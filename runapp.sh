#!/bin/bash

# export FLASK_DEBUG=True
export FLASK_APP=csfashionadvice/csfashionadvice.py
export FLASK_DEBUG=1
export CSFASHIONADVICE_SETTINGS=config.py
flask run
