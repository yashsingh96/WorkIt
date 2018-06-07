"""
csfashionadvice package initializer.
"""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (csfashionadvice/config.py)
app.config.from_object('csfashionadvice.config')

app.config.from_envvar('CSFASHIONADVICE_SETTINGS', silent=True)


# Tell our app about views and model.  This is dangerously close to a
# circular import, which is naughty, but Flask was designed that way.
# (Reference http://flask.pocoo.org/docs/0.12/patterns/packages/)  We're
# going to tell pylint and pycodestyle to ignore this coding style violation.
# import csfashionadvice.views  # noqa: E402  pylint: disable=wrong-import-position
