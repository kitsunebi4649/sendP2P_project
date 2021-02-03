import os
import requests
import utils
import time
import glob

RECIPIENT_IP = '192.168.0.11:5004'


if __name__ == '__main__':
    print(os.listdir('send_file'))
    full_filename_list = glob.glob('send_file/**', recursive=True)
    print(full_filename_list)
    filename_list = [name[len('send_file/'):] for name in full_filename_list]
    print(filename_list)
    for i, filename in enumerate(filename_list):  # このif文改良の余地あり
        if filename == '':
            del filename_list[i]  # .DS_Storeを削除。必ずif文の前 #隠しファイル無効
    print(filename_list)
    print(not filename_list == [])
    if not filename_list == []:
        print('list start', time.time())
        data_list = [utils.read_and_encode(filename) for filename in filename_list]
        print(filename_list)
        print('dict start', time.time())
        data = {k: v for k, v in zip(filename_list, data_list)}
        print('send start', time.time())
        requests.put(f'http://{RECIPIENT_IP}/test', json=data)
        print('send end', time.time())
    else:
        print('no file!!')
