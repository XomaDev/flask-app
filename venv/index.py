from flask import Flask

app = Flask(__name__)
text = ''

@app.route('/')
def home():
    return 'Home Page Route - nice work Andrew!!!'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'

@app.route('/api/send')
def send():
    message = request.args.get('text')
    global text
    text = message
    return 'True'


@app.route('/api/receive')
def receive():
    return text


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text
