from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    return time.ctime(time.time())
    #t = datetime.now()
    #return t.strftime("%H:%M:%S")

app.run(host='0.0.0.0',
        port=8080,
        debug=True)