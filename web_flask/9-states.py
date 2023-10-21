#!/usr/bin/python3
"""list of states by id"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display a HTML page that lists states"""
    states_dict = storage.all(State)
    if state_id:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states_dict, id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
