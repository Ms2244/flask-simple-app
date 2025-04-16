from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello_world():
    return '<h1>Home Page!</h1><p>Welcome to my Flask app!</p>'

@app.route('/about')
def about():
    return '<h1>About Page!</h1><p>This is a simple Flask application.</p>'

if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that returns "Hello, World!" when accessed at the root URL.