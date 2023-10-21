#!/usr/bin/python3
"""bnb filter"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display a HTML page that lists states"""
    states_dict = storage.all(State)
    amenities_dict = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states_dict, amenities=amenities_dict)

            
@app.teardown_appcontext
def teardown_db(exception):
    """remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
