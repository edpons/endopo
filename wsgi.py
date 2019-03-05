from flask import Flask
import requests, time, hashlib
from flask_cors import CORS

from twilio.rest import Client

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

@application.route('/trucada/<telefon>')
def trucada(telefon):
	account_sid = 'ACb10d8bc1e852d5695213adb0e2741026'
	auth_token = 'fd76d357c700546c40cf72c60b0da80e'
	client = Client(account_sid, auth_token)
	phone = '+34' + telefon
	call = client.calls.create(
		url='http://demo.twilio.com/docs/voice.xml',
		to=phone,
		from_='+34946665939'
	)
	print(call.to)
	return '^t3kn1r4p1d^'

if __name__ == "__main__":
    application.run()
