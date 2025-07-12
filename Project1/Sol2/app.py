from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, DevOps"

app.run(port=80) # 127.0.0.1
# app.run(host='0.0.0.0') # 기본은 5000 포트
# app.run(host='0.0.0.0', port=80)