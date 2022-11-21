from flask import Flask, session, render_template
import os

app = Flask(__name__)

app.config["DEBUG"] = True
app.config['SECRET_KEY'] = os.urandom(16) # 設定加密金鑰

@app.route("/session")
def setsession():
    session['My_session'] = 'Dan' # 製造session
    return 'My_session'

@app.route("/get") # get session
def getsession():
    get_session = session.get('My_session')
    return get_session

@app.route("/del") # del session
def delsession():
    # del session['My_session']
    # session.pop('My_session')
    session.clear()
    return "Delete session"

if __name__ == '__main__':
    app.run()