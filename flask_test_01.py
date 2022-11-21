"""
最簡單的錯誤代碼404使用方式
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index_html') # 首頁

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404 # 錯誤回傳

if __name__ == '__main__':
    app.run()