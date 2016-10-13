#!/usr/bin/env python

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hi', methods=['GET','POST'])
def hello_world():
    print('request.data', request.data)
    return 'request.data.get_data() = ' + request.get_data().decode('utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
