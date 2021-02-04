import requests
import utils

RECIPIENT_IP = '192.168.0.12:5004'
ZIP = True


if __name__ == '__main__':
    if not utils.get_filename_list('send_file/') == []:
        utils.to_zip(ZIP)
        print(utils.get_filename_list('send_file/'))
        requests.put(f'http://{RECIPIENT_IP}/test', json=utils.make_send_data(ZIP))
    else:
        print('no file!!')
