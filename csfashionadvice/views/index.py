"""
CS Fashion Advice index view.
"""

from flask import Flask
from flask import request
import csfashionadvice

@csfashionadvice.app.route('/', methods=['GET', 'POST'])
def show_index():
    if request.method == 'POST':
