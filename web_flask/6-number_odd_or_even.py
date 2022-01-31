#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
/c/<text>
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, render_template

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
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_py(text="is cool"):
    """ display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
    """
    if text:
        return "Python {}".format(text.replace("_", " "))
    else:
        return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def integer(n):
    if n:
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def templates(n):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd(n):
    """ /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
