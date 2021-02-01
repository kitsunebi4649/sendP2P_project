import requests
from flask import Flask
import base64

app = Flask(__name__)


response = requests.get('http://192.168.0.15:5004/test')  # blockchain.pyの222行目参照
response_json = response.json()
if response.status_code == 200:
    chain = response_json
    print(chain)

    with open("python-logo2.png", 'bw') as f4:
        f4.write(base64.b64decode(chain))
