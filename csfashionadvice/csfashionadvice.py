"""
CS Fashion Advice index view.
"""
import flask
from flask import Flask, url_for, redirect
from werkzeug import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'uploads'
)
print(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def show_index():
    return flask.render_template("index.html")


@app.route('/score', methods=['GET', 'POST'])
def score_image():
    if flask.request.method == 'POST':
        file = ''
        try:
            file = flask.request.files['image']
        except KeyError:
            context = {'error': 'Please upload a photo.'}
            return flask.render_template("index.html", **context)

        if not file:
            print("Should not get here.")

        filename = secure_filename(file.filename)
        filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filename)

        context = {'filename': os.path.abspath(filename), 'score': 0}
        return flask.render_template("score.html", **context)
    else:
        return redirect(url_for('show_index'))


if __name__ == '__main__':
    app.run()
