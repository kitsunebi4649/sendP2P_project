import requests
from flask import Flask
import utils

MY_PORT = 5004  # 同じデバイスならreceiver_server.port
NEW_FILENAME = 'SAMPLE2.png'

app = Flask(__name__)


if __name__ == '__main__':
    response = requests.get(f'http://127.0.0.1:{MY_PORT}/test')  # blockchain.pyの222行目参照
    response_json = response.json()
    if response.status_code == 200:
        data = response_json
        print(data)
        utils.decode_and_write(new_filename=NEW_FILENAME, data=data)


