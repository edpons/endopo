from flask import Flask
import requests
import time, hashlib

app = Flask(__name__)

api_key='emnrkrz4eetfaz6mgw7d5976'
secret='RPPZsj4629'
sigStr = "%s%s%d" % (api_key,secret,int(time.time()))
signature = hashlib.sha256(sigStr.encode('utf-8')).hexdigest()

headers={
'Api-Key': api_key, 
'X-Signature': signature
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/aa')
def hotels():
	url='https://api.test.hotelbeds.com/hotel-content-api/1.0/hotels/1?language=CAT&useSecondaryLanguage=false'
	r = requests.get(url, headers=headers)
	return r.text

if __name__ == "__main__":
    app.run()
