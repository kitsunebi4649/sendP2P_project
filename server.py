from flask import Flask
from flask import jsonify
from flask import request
import time
import utils

app = Flask(__name__)
message = None


@app.route('/test', methods=['PUT', 'GET'])
def receive():
    global message
    if request.method == 'PUT':
        print('put start', time.time())
        message = request.json
        print('put end', time.time())
        # with open('eee.txt', 'w')as e:
        #     e.write('kfdjskndnfsi')
        for k, v in message.items():
            utils.decode_and_write(new_filename=k, data=v)
        print('decode end', time.time())
        return jsonify({'message': 'success'}), 200

    if request.method == 'GET':  # blockchain_serverの27行目参照
        response = message
        return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5004,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    request_json = 0
    app.config['port'] = port

    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
