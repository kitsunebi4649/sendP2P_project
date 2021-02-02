import requests
import utils

FILE_NAME = 'SAMPLE.png'
RECIPIENT_IP = '192.168.0.6:5004'


if __name__ == '__main__':
    data = utils.read_and_encode(FILE_NAME)
    requests.put(f'http://{RECIPIENT_IP}/test', json=data)