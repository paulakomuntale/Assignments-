from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for sessions

# Sample user database (in real app, use a real database)
users = {
    'admin': 'password123',
    'user': 'pass123',
    'john': 'john123'
}

# ==================== LOGIN ROUTES ====================

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists and password matches
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error='Invalid username or password!')
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register')
def register():
    return "<h1>Registration Page - Coming Soon!</h1>"

# ==================== OTHER ROUTES ====================

@app.route('/about')
def about():
    return "<h1>this is about page</h1>"

@app.route('/contact')
def contact():
    return "<h1>this is contact page</h1>"

# Profile dynamic route
@app.route('/user/<string:username>/<int:user_id>')
def profile(username, user_id):
    # Data being passed from python to template
    return render_template('profile.html', username=username, user_id=user_id)

@app.route('/home')
def home_page():
    return "<h1>this is home page</h1>"

@app.route('/mystory/<name>')
def my_story(name):
    return f"<h1>This is my story, {name}!</h1>"

# ==================== RUN APP ====================

if __name__ == '__main__':
    app.run(debug=True)