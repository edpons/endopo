from flask import Flask
import requests
import time, hashlib

application = Flask(__name__)



@application.route('/')
def hello_world():
    return 'Hello, World!'

@application.route('/aa')
def hotels():
	api_key='emnrkrz4eetfaz6mgw7d5976'
	secret='RPPZsj4629'
	sigStr = "%s%s%d" % (api_key,secret,int(time.time()))
	signature = hashlib.sha256(sigStr.encode('utf-8')).hexdigest()

	headers={
		'Api-Key': api_key, 
		'X-Signature': signature
	}

	url='https://api.test.hotelbeds.com/hotel-content-api/1.0/hotels/2?language=CAT&useSecondaryLanguage=false'
	r = requests.get(url, headers=headers)
	r.headers['Access-Control-Allow-Origin'] = '*'
	return r.text

if __name__ == "__main__":
    application.run()
