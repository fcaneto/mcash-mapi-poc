## mCASH MAPI PoC app

This is a simple app to evaluate mCASH usage within a e-commerce web app.

#### Running local

1. Clone this repo
2. Tunnel ngrok to localhost:8000
3. Configure HOST_DOMAIN variable in .env with
4. Setup app database, running:
.1. ./syncdb.sh
.2. ./migrate.sh
5. ./run.sh

[Play with the mCASH testbed.](http://mcashtestbed.appspot.com/testbed/login/?token=A8_0ie3jUVq2TJ252W42L52DbSnZlWHWIsHkMjYWTdE)