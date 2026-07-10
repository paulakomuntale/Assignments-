from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>welcome to flask framework</h1>"

@app.route('/about')
def about():
    return "<h1>this is about page</h1>"

@app.route('/contact')
def contact():
    return "<h1>this is contact page</h1>"

@app.route('/home')
def home_page():
    return "<h1>this is home page</h1>"

@app.route('/mystory/<name>')
def my_story(name):
    return f"<h1>This is my story, {name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)