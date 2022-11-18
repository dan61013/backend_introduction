from flask import Flask
from flask import url_for # 回傳路徑
from flask import redirect # 重新導向
from flask import render_template # 渲染頁面

app = Flask(__name__)
# app.config.from_pyfile("configs.py")

@app.route("/") # 根目錄
def home():
    return "Hello World!"

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

if __name__ == '__main__':
    app.run()