import json

from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from mcash.mapi_client import MapiClient
from mcash.mapi_client.auth import SecretAuth
from settings import MCASH_MERCHANT_ID, MCASH_USER, MCASH_USER_SECRET, \
    MCASH_TESTBED_TOKEN, HOST_DOMAIN, MCASH_SHORTLINK_ID

from models import MCashTransaction, ShoppingCart

# mCASH client
mcash = MapiClient(auth=SecretAuth(MCASH_USER_SECRET),
                       mcash_merchant=MCASH_MERCHANT_ID,
                       mcash_user=MCASH_USER,
                       base_url='https://mcashtestbed.appspot.com/merchant/v1',
                       additional_headers={
                           'X-Testbed-Token': MCASH_TESTBED_TOKEN
                       }, )

def home(request):
    if not request.session.get('cart_id'):
        session_cart = ShoppingCart()
        session_cart.save()
        request.session['cart_id'] = session_cart.id
    else:
        session_cart = ShoppingCart.objects.get(pk=request.session.get('cart_id'))

    return render_to_response('home.html',
                              {'mcash_shortlink_id':MCASH_SHORTLINK_ID,
                               'cart':session_cart},
                              context_instance=RequestContext(request))


@csrf_exempt
def do_payment_request(request):
    request_body = json.loads(request.body)

    # argstring is the id of the cart being paid
    cart_id = request_body['object']['argstring']
    cart = ShoppingCart.objects.get(pk=cart_id)
    cart.status = ShoppingCart.STATUS_WAITING
    cart.save()

    transaction = MCashTransaction()
    transaction.customer_token = request_body['object']['id']
    transaction.shopping_cart = cart
    transaction.save()

    callback_url = 'https://' + HOST_DOMAIN + reverse('mcash_store.views.payment_response')
    response = mcash.create_payment_request(callback_uri=callback_url,
                                            # mapi client expects an str object
                                            customer=transaction.customer_token.encode('ascii'),
                                            currency="NOK",
                                            amount=str(cart.amount),
                                            allow_credit=True,
                                            # mapi client expects an str object
                                            pos_id=str(transaction.shopping_cart.id),
                                            pos_tid=str(transaction.id),
                                            action='AUTH',
                                            expires_in=21600) # mapi client says it is required, doc says the opposite

    # TODO: handle different responses
    transaction.mcash_id = response['id']
    transaction.save()

    return HttpResponse()


@csrf_exempt
def payment_response(request):
    request_body = json.loads(request.body)
    mcash_transaction_id = request_body['object']['tid']

    authorized = request_body['meta']['event'] == u'payment_authorized'

    if authorized:
        #Capture transaction
        callback_url = 'https://' + HOST_DOMAIN + reverse('mcash_store.views.payment_capture_response')
        mcash.update_payment_request(tid=mcash_transaction_id.encode('ascii'),
                                     action='CAPTURE',
                                     callback_uri=callback_url,)

    return HttpResponse()


@csrf_exempt
def payment_capture_response(request):
    request_body = json.loads(request.body)

    mcash_transaction_id = request_body['object']['tid']
    transaction = MCashTransaction.objects.get(mcash_id = mcash_transaction_id)

    cart = transaction.shopping_cart
    cart.status = ShoppingCart.STATUS_PAID
    cart.save()

    return HttpResponse()

######################
# Simple RESTful API
######################
@require_http_methods(["POST"])
@csrf_exempt
def new_shopping_cart(request):
    session_cart = ShoppingCart()
    session_cart.save()
    request.session['cart_id'] = session_cart.id
    return HttpResponse()

@require_http_methods(["GET"])
@csrf_exempt
def shopping_cart(request, id):
    cart = ShoppingCart.objects.get(pk=id)
    return HttpResponse(json.dumps(cart.to_dict()), content_type="application/json")
