from flask import Flask
import requests, time, hashlib

application = Flask(__name__)

api_key='emnrkrz4eetfaz6mgw7d5976'
secret='RPPZsj4629'

@application.route('/')
def hello_world():
    #resp = Response("Foo bar baz")
    #resp.headers['Access-Control-Allow-Origin'] = '*'
    return 'Hello'

@application.route('/aa')
def hotels():
	
	sigStr = "%s%s%d" % (api_key,secret,int(time.time()))
	signature = hashlib.sha256(sigStr.encode('utf-8')).hexdigest()

	headers= {
		'Api-Key': api_key, 
		'X-Signature': signature
	}
	
	url='https://api.test.hotelbeds.com/hotel-content-api/1.0/hotels/2?language=CAT&useSecondaryLanguage=false'
	
	resp = request.get(url, headers=headers)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

if __name__ == "__main__":
    application.run()
