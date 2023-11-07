"""
自定義非標準HTTP錯誤代碼
"""

from flask import Flask, abort, request, render_template

import werkzeug

app = Flask(__name__)

class InsufficientStorage(werkzeug.exceptions.HTTPException):
    
    code = 1000
    description = 'Not enough storage space.'
    
def handle_bad_request(error):
    return '錯誤代碼:1000', 1000

app.register_error_handler(InsufficientStorage, handle_bad_request)

@app.route('/')
def login():
    raise InsufficientStorage()

if __name__ == '__main__':
    app.run()