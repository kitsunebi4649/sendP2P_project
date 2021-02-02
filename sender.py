import os
import requests
import utils

RECIPIENT_IP = '192.168.0.6:5004'


if __name__ == '__main__':
    filename_list = os.listdir('send_file')
    if not filename_list == []:
        filename_list.remove('.DS_Store')  # .DS_Storeを削除
        data_list = [utils.read_and_encode(filename) for filename in filename_list]
        print(filename_list)
        data = {k: v for k, v in zip(filename_list, data_list)}
        requests.put(f'http://{RECIPIENT_IP}/test', json=data)
    else:
        print('no file!!')
