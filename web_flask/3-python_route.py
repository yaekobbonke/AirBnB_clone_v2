#!/usr/bin/python3
"""
starts a Flask web application
The application is listening listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display "HBNB"
    /c/<text>: display “C ”, followed by the value of the text variable
     replace underscore _ symbols with a space
     /python/(<text>):display “Python”, followed by
     the value of the text variable:
     replace underscore _ symbols with a space
     The default value of text is “is cool”
     must use the option 'strict_slashes=False' in route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """displays "Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    displays the value of c followed by text
    """
    text = replace(_, " ")
    return "c {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/(<text>", strict_slashes=False)
def python(text="is cool"):
    """
    displays the value of python followed by text
    """
    text = replace(_, " ")
    return "python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
