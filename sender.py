import os
import requests
import utils
import time

RECIPIENT_IP = '192.168.0.11:5004'


if __name__ == '__main__':
    filename_list = os.listdir('send_file')
    if '.DS_Store' in filename_list:
        filename_list.remove('.DS_Store')  # .DS_Storeを削除。必ずif文の前
    print(not filename_list == [])
    if not filename_list == []:
        print('list start',time.time())
        data_list = [utils.read_and_encode(filename) for filename in filename_list]
        print(filename_list)
        print('dict start', time.time())
        data = {k: v for k, v in zip(filename_list, data_list)}
        print('send start', time.time())
        requests.put(f'http://{RECIPIENT_IP}/test', json=data)
        print('send end', time.time())
    else:
        print('no file!!')
