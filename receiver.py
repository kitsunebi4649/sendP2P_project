import requests
from flask import Flask
import utils
import time

MY_PORT = 5004  # 同じデバイスならreceiver_server.port

app = Flask(__name__)


if __name__ == '__main__':
    response = requests.get(f'http://127.0.0.1:{MY_PORT}/test')  # blockchain.pyの222行目参照
    print('response start', time.time())
    response_json = response.json()
    print('response end', time.time())
    if response.status_code == 200:
        print('data start', time.time())
        data = response_json
        print('decode start', time.time())
        for k, v in data.items():
            utils.decode_and_write(new_filename=k, data=v)
        print('decode end', time.time())
