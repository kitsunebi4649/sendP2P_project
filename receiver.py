import requests
from flask import Flask

app = Flask(__name__)


response = requests.get('http://192.168.0.6:5004/test')  # blockchain.pyの222行目参照
response_json = response.json()
if response.status_code == 200:
    chain = response_json
    print(chain)




