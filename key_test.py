import time
from termcolor import cprint

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES


class Send_text(object):

    def __init__(self, data, public_key):
        self.data = data
        self.message_key = get_random_bytes(32)
        self.rsa_ciphertext = self.rsa_encrypt(public_key)
        self.aes_ciphertext, self.tag, self.nonce = self.aes_encrypt()

    def rsa_encrypt(self, public_key):
        # メッセージを暗号化
        public_cipher = PKCS1_OAEP.new(public_key)
        rsa_ciphertext = public_cipher.encrypt(self.message_key)
        return rsa_ciphertext

    def aes_encrypt(self):
        # 暗号化処理
        cipher = AES.new(self.message_key, AES.MODE_EAX)
        aes_ciphertext, tag = cipher.encrypt_and_digest(self.data)
        return aes_ciphertext, tag, cipher.nonce


class Received_text(object):

    def __init__(self, rsa_ciphertext, aes_ciphertext, tag, nonce, private_key):
        self.rsa_ciphertext = rsa_ciphertext
        self.aes_ciphertext = aes_ciphertext
        self.tag = tag
        self.nonce = nonce
        self.private_key = private_key
        self.message_key = self.rsa_decrypt()
        self.data = self.aes_decrypt()

    def rsa_decrypt(self):
        # メッセージを復号
        private_cipher = PKCS1_OAEP.new(self.private_key)
        message_key = private_cipher.decrypt(self.rsa_ciphertext)
        return message_key

    def aes_decrypt(self):
        # 復号処理
        cipher_dec = AES.new(self.message_key, AES.MODE_EAX, self.nonce)
        dec_data = cipher_dec.decrypt_and_verify(self.aes_ciphertext, self.tag)
        return dec_data

    def save(self, filename):
        with open(filename, 'bw') as s:
            s.write(self.data)


class Receiver(object):
    def __init__(self):
        self.private_key = RSA.generate(2 ** 10)
        self.public_key = my_private_key.publickey()


class Sender(object):
    def __init__(self):
        self.private_key = RSA.generate(2 ** 10)
        self.public_key = my_private_key.publickey()


def get_func_time(func):
    cprint(f'### {func.__name__} start ###', 'green')
    now = time.time()
    func()
    cprint(f'time: {time.time() - now} sec', 'cyan')
    cprint(f'### {func.__name__} end ###\n\n', 'green')


if __name__ == '__main__':
    my_private_key = RSA.generate(2 ** 10)
    my_public_key = my_private_key.publickey()

    with open('server.m4v', 'br') as r:
        dat = r.read()

    c = Send_text(dat, my_public_key)
    # print('ciphertext', c.aes_ciphertext.decode(errors='replace'))
    # print('tag', c.tag.decode(errors='replace'))
    # print('cipher.nonce', c.nonce.hex())
    # print('message_key', c.message_key.hex())

    d = Received_text(c.rsa_ciphertext, c.aes_ciphertext, c.tag, c.nonce, my_private_key)
    # print('message_key', d.message_key.hex())
    # print(d.data)
    # print(c.data, d.data)
    d.save('test_video.m4v')
