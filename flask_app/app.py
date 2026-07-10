from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>welcome to flask framework</h1>"

@app.route('/about')
def about():
    return "<h1>this is about page</h1>"

@app.route('/contact')
def contact(name):
    return "<h1>this is contact page</h1>"

@app.route('/home')
def home_page():  # THIS MUST BE DIFFERENT from 'home'
    return "<h1>this is home page</h1>"

if __name__ == '__main__':
    app.run(debug=True)