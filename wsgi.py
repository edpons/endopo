from flask import Flask
import requests, time, hashlib
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

api_key='emnrkrz4eetfaz6mgw7d5976'
secret='RPPZsj4629'

url_prefix='https://api.test.hotelbeds.com'

def headers():
	sigStr = "%s%s%d" % (api_key,secret,int(time.time()))
	signature = hashlib.sha256(sigStr.encode('utf-8')).hexdigest()

	headers= {
		'Api-Key': api_key, 
		'X-Signature': signature
	}
	return headers

@application.route('/')
def hello_world():
	#resp = Response("Foo bar baz")
	#resp.headers['Access-Control-Allow-Origin'] = '*'
	return 'Hello'

if __name__ == "__main__":
    application.run()
