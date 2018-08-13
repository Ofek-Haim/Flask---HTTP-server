from flask import Flask
from flask import request


app = Flask(__name__)


#index
@app.route('/')
def index():
    client_ip = request.remote_addr
    return "Your ip is: " + client_ip


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
