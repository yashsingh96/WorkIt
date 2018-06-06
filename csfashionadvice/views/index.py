"""
CS Fashion Advice index view.
"""

import os
from flask import Flask, resquest
import csfashionadvice

UPLOAD_FOLDER = os.path.basename('uploads')
csfashionadvice.app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@csfashionadvice.app.route('/')
def show_index():
    return flask.render_template("index.html")

@csfashionadvice.app.route('/score', methods=['POST'])
def score_image():
    image = request.files['image']
    f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(f)

    context = {'filename': f, 'score': score}
    return flask.render_template("score.html", **context)
