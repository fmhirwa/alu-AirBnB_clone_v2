#!/usr/bin/python3
"""Filter"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display HBNB"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities)


@app.teardown_appcontext
def teardown_db(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    