from wateraware import app
from flask import render_template, request, url_for
from flask_googlemaps import Map
from .utils import *
import json

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.form:
        loc = request.form['location']
        polys, meta = get_polys(loc)
        # meta = get_meta(loc)
        return render_template('polygon.html', polys=json.dumps(polys), meta=meta)
    else:
        return render_template('polygon.html')

@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')