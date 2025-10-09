from market import app  #<-- when we access the package it auto run __init__, tha's why we don't need to write market.__init__
from flask import render_template
from market.models import Item
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items=Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register')
def register_page():
    forms=RegisterForm()
    return render_template('register.html', forms=forms)

@app.route('/78805575')
def img78805575_page():
    return render_template('78805575.webp')

                           

