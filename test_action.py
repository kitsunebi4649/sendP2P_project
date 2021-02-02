import os
import time

if os.path.exists('receive_file/sample.txt'):
    os.remove('receive_file/sample.txt')
if os.path.exists('send_file/sample.txt'):
    os.remove('send_file/sample.txt')
with open('send_file/sample.txt', 'w') as f:
    # f.write('B'*(2**28))  # 268.44MB分
    # f.write('B'*(2**30))  # 1.07GB分。ファイルにおける転送速度はそれぞれ63秒。ただしbase64によってファイルサイズが大きくなっている。
    print('write start', time.time())
    f.write('B'*(2**5))
    print('write end', time.time())  # 2sec
