import os
import requests
import utils

RECIPIENT_IP = '192.168.0.6:5004'


if __name__ == '__main__':
    filename_list = os.listdir('send_file')
    print(filename_list)
    if not filename_list == []:
        data = utils.read_and_encode(filename_list[0])
        requests.put(f'http://{RECIPIENT_IP}/test', json=data)
    else:
        print('no file!!')