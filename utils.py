import base64


def read_and_encode(filename):
    with open(filename, 'br') as f1:
        b64_img = base64.b64encode(f1.read())
    send_data = b64_img.decode()
    return send_data


def decode_and_write(new_filename, data):
    with open(new_filename, 'bw') as f4:
        f4.write(base64.b64decode(data))
