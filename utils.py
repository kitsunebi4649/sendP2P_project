import base64
import time
import zipfile
import glob


def read_and_encode(filename, is_zip):
    print('encode start', time.time())
    if is_zip:
        with open(f'send_file_zip/{filename}.zip', 'br') as f1:
            b64_img = base64.b64encode(f1.read())
    else:
        with open(f'send_file/{filename}', 'br') as f1:
            b64_img = base64.b64encode(f1.read())
    send_data = b64_img.decode()
    print('encode end', time.time())
    return send_data


def decode_and_write(new_filename, data, is_zip):
    if is_zip:
        with open(f'receive_file_zip/{new_filename}.zip', 'bw') as f4:
            f4.write(base64.b64decode(data))                           # TODO
    else:
        with open(f'receive_file/{new_filename}', 'bw') as f4:
            f4.write(base64.b64decode(data))


def get_filename_list(head_dir_name=''):
    full_filename_list = glob.glob('send_file/**', recursive=True)
    before = [name[len(head_dir_name):] for name in full_filename_list]
    for i, filename in enumerate(before):  # このif文改良の余地あり
        if filename == '':
            del before[i]  # .DS_Storeを削除。必ずif not filename_list == []:文の前 #隠しファイル無効
    return before


def to_zip(is_zip):
    # print(os.listdir('send_file_zip'))
    # for r in glob.glob('send_file_zip/**', recursive=True):
    #     print(r)
    #     os.remove(r)
    if is_zip:
        for filename in get_filename_list('send_file/'):
            with zipfile.ZipFile(f'send_file_zip/{filename}.zip', 'w') as z:  # 新規zipファイル名
                # for f in get_filename_list('send_file/'):  # zip対象ファイル名 ディレクトリーは無効
                # print(get_filename_list('send_file/'))
                z.write('send_file/' + filename)


def make_send_data(is_zip):
    return {'filename_list': get_filename_list('send_file/'), 'data': [read_and_encode(filename=filename,
            is_zip=is_zip)for filename in get_filename_list('send_file/')], 'is_zip': is_zip}


def to_unzip(filename_list, is_zip):
    if is_zip:
        for filename in filename_list:
            print(f'receive_file_zip/{filename}')
            with zipfile.ZipFile(f'receive_file_zip/{filename}.zip', 'r')as f:
                f.extractall('receive_file')


        # with zipfile.ZipFile('receive_file_zip/send.zip', 'r') as f:
        #     f.extractall('.')  # ファイル全体をrename
