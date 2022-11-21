from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/cookie") # 製造cookie
def setcookie():
    response = make_response('My cookie')
    response.set_cookie(key='My_cookie', value='Hello')
    return response

@app.route("/get") # 取得cookie
def getcookie():
    get_cookie = request.cookies.get('My_cookie')
    return get_cookie

@app.route("/del") # 刪除cookie
def delcookie():
    response = make_response('Delete cookies')
    response.set_cookie(key='My_cookie', value='', expires=0)
    return response

if __name__ == '__main__':
    app.run()