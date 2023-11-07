"""
錯誤404 + if條件判斷輸入值
"""
from flask import Flask, request, render_template, abort

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login2.html')

@app.route("/hello", methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        if request.values['username'] == 'Dan':
            return 'Hello ' + request.values['username']
        else:
            abort(404) # 產生錯誤

@app.errorhandler(404)
def page_not_found(error):
    return 'This page {} does not exist'.format(request.values['username']), 404

if __name__ == '__main__':
    app.run()