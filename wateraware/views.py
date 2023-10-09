from wateraware import app
from flask import render_template, request
from flask_googlemaps import Map
from .utils import *
import json

@app.route("/", methods=['GET', 'POST'])
def home():
    loc = request.form['location']
    info, polys = get_polys(loc)
    meta = get_meta(loc)
    # print(meta)
    return render_template('polygon.html', info=info, polys=json.dumps(polys), meta=meta)