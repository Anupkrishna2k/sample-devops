from flask import Flask

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello Anup, DevOps in progress,Welcome to 2.0 🚀"

import os

@app.route("/")
def hello():
    return os.getenv("APP_MESSAGE", "Default Message")

@app.route("/secret")
def secret():
    return os.getenv("SECRET_MESSAGE", "No Secret")

@app.route("/health")
def health():
    return "COOL OK" 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
