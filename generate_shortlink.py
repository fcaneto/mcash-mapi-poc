import os
import json
import logging


from mcash.mapi_client import MapiClient
from mcash.mapi_client.auth import SecretAuth

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logging.getLogger("mcash.mapi_client.mapi_client").addHandler(ch)

if __name__ == "__main__":
    MCASH_MERCHANT_ID = os.getenv('MCASH_MERCHANT_ID')
    MCASH_USER = os.getenv('MCASH_USER')
    MCASH_USER_SECRET = os.getenv('MCASH_USER_SECRET')
    MCASH_TESTBED_TOKEN = os.getenv('MCASH_TESTBED_TOKEN')
    HOST_DOMAIN = os.getenv('HOST_DOMAIN')

    # mCASH client
    mcash = MapiClient(auth=SecretAuth(MCASH_USER_SECRET),
                       mcash_merchant=MCASH_MERCHANT_ID,
                       mcash_user=MCASH_USER,
                       base_url='https://mcashtestbed.appspot.com/merchant/v1',
                       additional_headers={
                           'X-Testbed-Token': MCASH_TESTBED_TOKEN
                       }, )

    callback_url = 'https://' + HOST_DOMAIN + '/pay/'
    response = mcash.create_shortlink(callback_url)

    if response:
        print 'Shortlink created with id %s.' % response['id']

