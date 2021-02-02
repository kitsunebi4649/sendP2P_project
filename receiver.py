import requests
from flask import Flask
import utils

MY_PORT = 5004  # 同じデバイスならreceiver_server.port

app = Flask(__name__)


if __name__ == '__main__':
    response = requests.get(f'http://127.0.0.1:{MY_PORT}/test')  # blockchain.pyの222行目参照
    response_json = response.json()
    if response.status_code == 200:
        data = response_json['data']
        new_filename = response_json['filename']
        print(data)
        for k, v in zip(new_filename, data):
            utils.decode_and_write(new_filename=k, data=v)
