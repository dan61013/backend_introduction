from flask import Flask, Request
from flask import url_for # 回傳路徑
from flask import redirect # 重新導向
from flask import render_template # 渲染頁面
from flask import request

app = Flask(__name__)
# app.config.from_pyfile("configs.py")

# @app.route("/") # 根目錄
# def home():
#     return "Hello World!"

@app.route("/test1")
def test1():
    # return url_for('home')
    return redirect('http://127.0.0.1:5000/')

@app.route("/test2")
def test2():
    return redirect(url_for('test1'))

@app.route("/index")
def index():
    return render_template('index.html', username='Dan')

@app.route("/<user>")
def test3(user):
    return render_template('index.html', username='Dan')

@app.route("/")
def login():
    return render_template('login2.html')

@app.route("/hello", methods=['GET', 'POST']) # methods 路由的允許方式
def hello():
    if request.method == 'POST':
        # return 'Hello ' + request.args['username'] # args取得前端的username, 使用GET方式
        # return 'Hello ' + request.form['username'] # 使用POST方式, 取form
        return 'Hello ' + request.values['username'] # 使用POST方式, 取values

if __name__ == '__main__':
    app.run()