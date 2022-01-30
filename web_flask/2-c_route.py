#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
/c/<text>
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Return the message: "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def second_hello():
    """
    Return the message: "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_h(text):
    """ display “C ” followed by the value
    of the text variable (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
