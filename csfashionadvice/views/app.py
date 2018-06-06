"""
CS Fashion Advice index view.
"""

import os

import flask
from flask import request

import csfashionadvice

UPLOAD_FOLDER = os.path.basename('uploads')
csfashionadvice.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@csfashionadvice.app.route('/')
def show_index():
    return flask.render_template("index.html")


@csfashionadvice.app.route('/score', methods=['POST'])
def score_image():
    file = request.files['image']
<<<<<<< HEAD
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
=======
    f = os.path.join(flask.app.config['UPLOAD_FOLDER'], file.filename)
>>>>>>> 57b83140137ec45193811e2d7b3553214cb86b06

    file.save(f)
    score = 0

    context = {'filename': f, 'score': 0}
    return flask.render_template("score.html", **context)
