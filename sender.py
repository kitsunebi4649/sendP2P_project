import os
import requests
import utils

RECIPIENT_IP = '192.168.0.6:5004'


if __name__ == '__main__':
    filename_list = os.listdir('send_file')
    filename_list.remove('.DS_Store')  # .DS_Storeを削除
    print(filename_list)
    # data_list = []
    # for filename in filename_list:
    #     data_list.append(utils.read_and_encode(filename))
    data_list = [utils.read_and_encode(filename) for filename in filename_list]
    if not filename_list == []:
        data = {'data': data_list,
                'filename': filename_list
                }  # 個々でリストにするか検討する
        requests.put(f'http://{RECIPIENT_IP}/test', json=data)
    else:
        print('no file!!')
