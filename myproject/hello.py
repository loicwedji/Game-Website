from flask import Flask

from myproject.test import messageT


app = Flask(__name__) 

@app.route('/')
def hello_world():
    return "<h1>It's Working</h1>"

@app.route('/Home')
def home_page():
    return "<button type ='button'>We are home</button>" 

@app.route('/data')
def data_page():
  return messageT()
