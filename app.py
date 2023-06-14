from flask import Flask,url_for
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return '<h2>Welcome to my HomePage!</h2><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/test')
def test_url_for():
    print(url_for('index'))
    print(url_for('user_page', name='bruce'))
    print(url_for('user_page', name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'
