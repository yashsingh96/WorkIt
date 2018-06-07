"""
CS Fashion Advice development configuration.
"""

import os

# Root of this application
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
# SECRET_KEY = b'\xb6@\xcdd\xc4\x7fI\x8aj.N\x88\xea\xf6M\x96`t\x8c\xe9Q\x9f\\\x18'
# SESSION_COOKIE_NAME = 'login'

# File uploads to 'uploads/'
# UPLOAD_FOLDER = os.path.join(
#     os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'uploads'
# )

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
