import base64
import receiver


def encoder():
    with open("python-logo.png", 'br') as f1:
        b64_img = base64.b64encode(f1.read())

    with open("python-logo.txt", "w") as f2:
        f2.write(b64_img.decode())


def decoder():
    # with open("python-logo.txt", 'r') as f3:
    #     data = f3.read()

    data = receiver.chain

    with open("python-logo2.png", 'bw') as f4:
        f4.write(base64.b64decode(data.encode()))
