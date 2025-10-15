from market import app, db  #<-- when we access the package it auto run __init__, tha's why we don't need to write market.__init__
from flask import render_template, url_for, redirect, flash
from market.models import Item, User
from market.forms import RegisterForm

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items=Item.query.all()
    return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    forms=RegisterForm()
    if forms.validate_on_submit():
        user_to_create=User(username=forms.username.data,
                            email_address=forms.email_address.data,
                            password=forms.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if forms.errors != {}: # Print the error messages on the server side.
        for error in forms.errors.values():
            flash(f'Error creating user: {error}', category='danger')
    return render_template('register.html', forms=forms)
                           

