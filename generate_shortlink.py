import os
import json

from mcash.mapi_client import MapiClient
from mcash.mapi_client.auth import SecretAuth

if __name__ == "__main__":
    MERCHANT_ID = os.getenv('MERCHANT_ID')
    MCASH_USER = os.getenv('MCASH_USER')
    MCASH_USER_SECRET = os.getenv('MCASH_USER_SECRET')
    TESTBED_TOKEN = os.getenv('TESTBED_TOKEN')
    HOST_DOMAIN = os.getenv('HOST_DOMAIN')

    # mCASH client
    mcash = MapiClient(auth=SecretAuth(MCASH_USER_SECRET),
                       mcash_merchant=MERCHANT_ID,
                       mcash_user=MCASH_USER,
                       base_url='https://mcashtestbed.appspot.com/merchant/v1',
                       additional_headers={
                           'X-Testbed-Token': TESTBED_TOKEN
                       }, )

    

    if response:
        print 'Shortlink created with id %s.' % response['id']

