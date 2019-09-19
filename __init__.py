from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Z3HomuOuDX'
app.config['DEV_EMAIL'] = 'adrienshen.dev@gmail.com'
app.config['AMAZON_AFFILIATE_TOKEN'] = ''

from app import routes
