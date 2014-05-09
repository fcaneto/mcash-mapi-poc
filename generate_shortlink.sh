URL=https://$1/pay/
echo Creating shortlink to $URL

curl -i -X POST \
-H 'Accept: application/vnd.mcash.api.merchant.v1+json' \
-H 'Content-Type: application/json' \
-H 'X-Mcash-Merchant: iw1yhe' \
-H 'X-Mcash-User: thedude' \
-H 'Authorization: SECRET supersecret' \
-H 'X-Testbed-Token: A8_0ie3jUVq2TJ252W42L52DbSnZlWHWIsHkMjYWTdE' \
-d '{"callback_uri":"$URL"}' \
https://mcashtestbed.appspot.com/merchant/v1/shortlink/


