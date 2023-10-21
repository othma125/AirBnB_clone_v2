#!/usr/bin/python3
"""list of states"""
from flask import Flask, render_template
from models import storage
from models.state import state
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
	"""display a HTML page"""
	states = storage.all(State)
	return render_template('7-states_list.html', states=states.values())
