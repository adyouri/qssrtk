# -*- coding: utf8 -*-

########################################################
#                                                      #
# Name       : Qssrtk                                  #
#                                                      #
# Description: A lightweight Url shortener script      # 
#                                                      #
# Developer  : Abdelhadi Dyouri                        # 
#                                                      #
# Version    : 1.0                                     #
#                                                      #
########################################################

# Imports
from flask import Flask, redirect, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids
import os

# Config
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db' 
SALT = 'Hashids SALT GOES HERE'

# Models
class Url(db.Model):
    # Create table `urls` |id|url|
    __tablename__ = "urls"
    id = db.Column(db.Integer, primary_key=True) 
    url = db.Column(db.Text)

    def __init__(self, url):
        self.url = url


# Controllers
@app.route('/sh', methods = ['GET', 'POST'])
def sh():
    # If it's a POST request:
    if request.method == 'POST':
        # Get link from HTML form
        link = request.args.get('link')
        # Basic link checker
        if link != "" and not link.count(' ') >= 1 and not link.count('.') == 0:
            # Add link to the Database
            if link[:4] != 'http':
                link = 'http://{}'.format(link)
            db.session.add(Url(url=link)) 
            db.session.commit()
            # Get last added id
            url_id = db.session.query(Url).order_by(Url.id.desc()).first().id
            # Encode id (example: 3 => HFdK)
            id_code = Hashids(salt=SALT, min_length=4).encode(url_id)
            # Generate short link ('/HFdK')
            short_link = '/' + id_code  
            # Make a dictionary {'url_id': 3, 'short_link': '/HFdK'}
            urls = dict(url_id=url_id, short_link=short_link)
            # Convert urls dictionary to JSON and return it
            return jsonify(**urls) 
        else:
            return jsonify(**{'url_id':0, 'short_link':''})

    return render_template('index.html', page='sh', short_link = 'qssrtk.herokuapp.com/kRa0')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<id>')
def url(id):
    # Decode id (HFdK => 3)}}
    original_id = Hashids(salt=SALT, min_length=4).decode(id)
    if original_id:
        original_id = original_id[0]
        # Get original url ('get url where id = original_id')
        original_url = Url.query.filter_by(id=original_id).first().url
        return redirect(original_url , code=302)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
