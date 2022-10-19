#pip install flask
from flask import Flask
#initialize the app
app=Flask(__name__)
@app.route("/")
def home():
    return "hello world"
#run the app
app.run() #created a server