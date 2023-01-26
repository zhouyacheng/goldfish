from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)
@app.route('/')
def hello():
    print(os.environ)
    CONTENT1 = os.environ.get("CONTENT1","hello world")
    CONTENT2 = os.environ.get("CONTENT2","hello world")
    print(f"CONTENT1: {CONTENT1} ,CONTENT2: {CONTENT2}",)
    return f'<h1>{CONTENT1} {datetime.now().strftime("%Y%m%d %H%M%S")} {CONTENT2}</h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=50001,debug=True)