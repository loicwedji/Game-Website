from flask import Flask


app = Flask(__name__) 

@app.route('/')
def hello_world():
    return "<h1>It's Working</h1>"

@app.route('/Home')
def home_page():
    return "<button type ='button'>We are home</button>"
