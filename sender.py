import os
import requests
import utils

RECIPIENT_IP = '192.168.0.6:5004'


if __name__ == '__main__':
    filename_list = os.listdir('send_file')
    filename_list.remove('.DS_Store')  # .DS_Storeを削除
    print(filename_list)
    if not filename_list == []:
        data = {'data': utils.read_and_encode(filename_list[0]),
                'filename': filename_list[0]
                }
        requests.put(f'http://{RECIPIENT_IP}/test', json=data)
    else:
        print('no file!!')
