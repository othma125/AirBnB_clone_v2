#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns Hello HBNB!"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Display 'C' followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def display_python_text(text):
    """Display 'python' followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Display 'n is a number' only if n is an integer. """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ Display a HTML page only if n is an integer. """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
