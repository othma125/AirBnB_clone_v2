#!/usr/bin/python3
"""list of states by id"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
#list all states
@app.route('/states/<id>', strict_slashes=False)
#list states that match the id
def states(id=None):
    """display a HTML page that lists states"""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
