from flask import Flask, render_template
app = Flask(__name__)

# Login Page
@app.route('/')
def index():
    return 'Hello, World!'

# Dashboard Page
@app.route('/user/<username>')
def show_dash(username):
    return render_template("dashboard.html", username=username)