"""
CS Fashion Advice index view.
"""
import flask
from flask import Flask, flash, session
import os

from flask_session import Session

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sess = Session()

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

sess.init_app(app)

app.debug = True


@app.route('/')
def show_index():
    return flask.render_template("index.html")


@app.route('/feedback')
def show_feedback_box():
    message = "Thanks for the feedback!"
    flash(message)
    return flask.render_template("test.html")


@app.route('/score', methods=['POST'])
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

        f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(f)

        context = {'filename': f, 'score': 0}
        return flask.render_template("score.html", **context)
    else:
        print("I DONT WANT TO GET HERE")


if __name__ == '__main__':
    app.run()
