import subprocess
import socket
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    global seed
    if request.method == 'POST':
        subprocess.run(["python3", "stress_cpu.py"])
        return "post"
    elif request.method == 'GET':
        private_ip = socket.gethostbyname(socket.gethostname())
        return f'Private IP address: {private_ip}\n', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
