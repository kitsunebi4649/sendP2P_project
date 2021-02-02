import base64
import time


def read_and_encode(filename):
    print('encode start', time.time())
    with open(f'send_file/{filename}', 'br') as f1:
        b64_img = base64.b64encode(f1.read())
    send_data = b64_img.decode()
    print('encode end', time.time())
    return send_data


def decode_and_write(new_filename, data):
    with open(f'receive_file/{new_filename}', 'bw') as f4:
        f4.write(base64.b64decode(data))
