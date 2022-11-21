from flask import Flask, abort, request, render_template, make_response

app = Flask(__name__)

@app.route('/str')
def str():
    response = make_response('Hello world!')
    return response

@app.route('/index')
def index():
    response = make_response(render_template('index.html'))
    return response

if __name__ == '__main__':
    app.run()