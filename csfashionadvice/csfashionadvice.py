"""
CS Fashion Advice index view.
"""
import os

import flask
from flask import Flask, url_for, redirect, flash

from classifier import get_style_score, get_appropriate_score

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'uploads'
)

app.secret_key = 'some_secret'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def show_index():
    return flask.render_template("index.html")


@app.route('/feedback')
def show_feedback():
    message = "Thanks for the feedback!"
    flash(message)
    return flask.render_template('test.html')


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

        filename = file.filename
        # f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # get gender from radio form submission
        gender = flask.request.form['gender']

        ascore = get_appropriate_score(filename, gender, False)

        score = get_style_score(filename, gender, filename != "nomatch.jpg")

        if ascore == 0 or ascore == 1:
            atext = "Wow! You're dressed to impress!"
        elif ascore == -1 and gender == "M":
            atext = "Hm... maybe, but consider wearing pants."
        elif ascore == -3:
            atext = "You're pushing it, but the Capital One attire saves you."
        else:
            atext = "Um, let's take this offline..."



        if score == 0:
            stext = "Stunning!"
        if score == -1:
            stext = "Take another look in the mirror."


        context = {'filename': filename, 'score': stext, 'ascore': atext}
        return flask.render_template("score.html", **context)
    else:
        return redirect(url_for('show_index'))


# @app.route('/show/<filename>')
# def uploaded_file(filename):
#     filename = 'http://127.0.0.1:5000/uploads/' + filename
#     return render_template('template.html', filename=filename)

@app.route('/uploads/<filename>')
def send_file(filename):
    return flask.send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run()
