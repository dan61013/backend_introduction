from flask import Flask

app = Flask(__name__)

# CONFIGS = {
#     "DEBUG": True
# }

app.config.from_pyfile('configs.py')
# app.config['DEBUG'] = True

@app.route("/")
def Hello():
    return "Hello world!"

if __name__ == '__main__':
    # app.debug = True
    app.run()