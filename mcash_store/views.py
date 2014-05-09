import json

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse

from mcash.mapi_client import MapiClient
from mcash.mapi_client.auth import SecretAuth
from settings import MERCHANT_ID, MCASH_USER, MCASH_USER_SECRET, TESTBED_TOKEN, HOST_DOMAIN

from models import MCashTransaction


def home(request):
    return render_to_response('home.html',
                              context_instance=RequestContext(request))


@csrf_exempt
def do_payment_request(request):
    request_body = json.loads(request.body)

    transaction = MCashTransaction()
    transaction.customer_token = request_body['object']['id']
    transaction.session_id = "1" # represents a 'POS', could be a session/shopping cart on web store scenario
    transaction.save()

    mcash = MapiClient(auth=SecretAuth(MCASH_USER_SECRET),
                       mcash_merchant=MERCHANT_ID,
                       mcash_user=MCASH_USER,
                       base_url='https://mcashtestbed.appspot.com/merchant/v1',
                       additional_headers={
                           'X-Testbed-Token': TESTBED_TOKEN
                       }, )

    callback_url = 'https://' + HOST_DOMAIN + reverse('mcash_store.views.payment_response')
    response = mcash.create_payment_request(callback_uri=callback_url,
                                            # mapi client expects an str object
                                            customer=transaction.customer_token.encode('ascii'),
                                            currency="NOK",
                                            amount="1.00",
                                            allow_credit=True,
                                            # mapi client expects an str object
                                            pos_id=transaction.customer_token.encode('ascii'),
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
        #transaction = MCashTransaction.objects.get(mcash_id = transaction_mcash_id)

        #Capture transaction
        mcash = MapiClient(auth=SecretAuth(MCASH_USER_SECRET),
                           mcash_merchant=MERCHANT_ID,
                           mcash_user=MCASH_USER,
                           base_url='https://mcashtestbed.appspot.com/merchant/v1',
                           additional_headers={
                               'X-Testbed-Token': TESTBED_TOKEN
                           }, )

        callback_url = 'https://' + HOST_DOMAIN + reverse('mcash_store.views.payment_capture_response')
        mcash.update_payment_request(tid=mcash_transaction_id.encode('ascii'),
                                     action='CAPTURE',
                                     callback_uri=callback_url,)

    return HttpResponse()


@csrf_exempt
def payment_capture_response(request):
    request_body = json.loads(request.body)
    print request_body

    # TODO: update ui

    return HttpResponse()
