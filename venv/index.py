from flask import Flask
from flask import Flask, request

app = Flask(__name__)
text = ''

@app.route('/')
def home():
    return 'Home Page Route - nice work Xoma!!!'

@app.route('/api/send')
def send():
    message = request.args.get('text')
    global text
    text = message
    return 'True'


@app.route('/api/receive')
def receive():
    return text

