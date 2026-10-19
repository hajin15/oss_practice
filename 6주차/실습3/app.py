from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    with open('/app/logs/access.log', 'a') as f:
        f.write(f"{datetime.datetime.now()} - {request.remote_addr}\n")
    return "Hello, Bind Mount!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)