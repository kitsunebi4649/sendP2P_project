from flask import Flask
from flask import jsonify
from flask import request
import utils
import os

DELETE_ALL_RECEIVE_DIR = False  # 再起動するバグ

app = Flask(__name__)
message = None


@app.route('/test', methods=['PUT', 'GET'])
def receive():
    global message
    utils.dir_reset('receive_file_zip')
    if request.method == 'PUT':
        message = request.json
        # if message['is_zip']:
        #     utils.decode_and_write(new_filename='send.zip', data=message['data'], is_zip=['is_zip'])
        # else:
        print(message['filename_list'])
        for k, v in zip(message['filename_list'], message['data']):
            utils.decode_and_write(new_filename=k, data=v, is_zip=message['is_zip'])
        utils.to_unzip(filename_list=message['filename_list'], is_zip=message['is_zip'])
        return jsonify({'message': 'success'}), 200

    if request.method == 'GET':  # blockchain_serverの27行目参照
        response = message
        return jsonify(response), 200


if __name__ == '__main__':
    if DELETE_ALL_RECEIVE_DIR and len(os.listdir('receive_file')) != 0:
        for i in os.listdir('receive_file'):
            os.remove(f'receive_file/{i}')
        print('all files removed!')
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5004,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    request_json = 0
    app.config['port'] = port

    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
