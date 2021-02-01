import requests
import encoder

# data = 123456787654323456
data = encoder.message

recipient_ip = '192.168.0.6:5004'
requests.put(f'http://{recipient_ip}/test', json=data)