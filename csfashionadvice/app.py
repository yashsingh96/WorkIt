"""
CS Fashion Advice index view.
"""

import os

import flask
import csfashionadvice

UPLOAD_FOLDER = os.path.basename('uploads')
csfashionadvice.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@csfashionadvice.app.route('/')
def show_index():
    return flask.render_template("index.html")


@csfashionadvice.app.route('/score', methods=['POST'])
def score_image():
    file = flask.request.files['image']
    f = os.path.join(flask.app.config['UPLOAD_FOLDER'], file.filename)
    file.save(f)

    context = {'filename': f, 'score': 0}
    return flask.render_template("score.html", **context)
