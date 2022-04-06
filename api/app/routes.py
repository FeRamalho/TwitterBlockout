from app import app
from app import auth
import time

@app.route('/index')
def index():
    a = "29"
    return a

@app.route('/oauth/reqtoken', methods=["GET"])
def get_request_token():
    result = auth.request_token()
    return result

@app.route('/time', methods=["GET"])
def get_current_time():
    return {'time': time.time()}