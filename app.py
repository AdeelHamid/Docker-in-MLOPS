# A flask application for greeting and asking for channel subscriptions
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():

    return '''<html>
                <head>
                    <title>Welcome</title>
                </head>
                <body>
                <form action="/greet" method="post">
                    <h1>Hello, Welcome to our channel!</h1>
                    <input type="text" name="name" placeholder="Enter your name">
                    
                    <input type="submit" value="Greet Me!">
                </form>
                </body>
            </html>'''

@app.route('/greet', methods=['POST'])
def greet():
    user_input = request.form['name']
    return f"Hello, {user_input}! Welcome to our channel. Please subscribe!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
