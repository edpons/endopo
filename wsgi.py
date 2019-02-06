from flask import Flask
import requests, time, hashlib
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

api_key='emnrkrz4eetfaz6mgw7d5976'
secret='RPPZsj4629'

@application.route('/')
def hello_world():
	#resp = Response("Foo bar baz")
	#resp.headers['Access-Control-Allow-Origin'] = '*'
	return 'Hello'

@application.route('/aa')
def hotel_():
	
	sigStr = "%s%s%d" % (api_key,secret,int(time.time()))
	signature = hashlib.sha256(sigStr.encode('utf-8')).hexdigest()

	headers= {
		'Api-Key': api_key, 
		'X-Signature': signature
	}
	
	url='https://api.test.hotelbeds.com/hotel-content-api/1.0/hotels/2?language=CAT&useSecondaryLanguage=false'
	
	r = requests.get(url, headers=headers)
	return r.text

@application.route('/hotels')
def hotels():
	sigStr = "%s%s%d" % (api_key,secret,int(time.time()))
	signature = hashlib.sha256(sigStr.encode('utf-8')).hexdigest()

	headers= {
		'Api-Key': api_key, 
		'X-Signature': signature
	}
	
	payload = {
		"stay": {
			"checkIn": "2019-06-08",
			"checkOut": "2019-06-10"
		},
		"occupancies": [
			{
				"rooms": 1,
				"adults": 2,
				"children": 1,
				"paxes": [
					{
						"type": "AD",
						"age": 30
					},
					{
						"type": "AD",
						"age": 30
					},
					{
						"type": "CH",
						"age": 8
					}
				]
			}
		],
		"hotels": {
			"hotel": [
				1067,1070,1075,135813,145214,1506,1508,1526,1533,1539,1550,161032,170542,182125,187939,212167,215417,228671,229318,23476
				]
	  }
	}
	
	url='https://api.test.hotelbeds.com/hotel-api/1.0/hotels'
	
	r = requests.post(url, headers=headers, data=payload)
	return r.text

if __name__ == "__main__":
    application.run()
