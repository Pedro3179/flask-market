from market import app, db  #<-- when we access the package it auto run __init__, tha's why we don't need to write market.__init__
from flask import render_template, url_for, redirect, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user

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

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form=LoginForm()
    if form.validate_on_submit():
        attempted_user=User.query.filter_by(email_address=form.email_address.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password1.data
        ):
            login_user(attempted_user)
            flash(f'Welcome, {attempted_user.email_address}.', category='success')
            return redirect(url_for('market_page'))
        else:
            flash(r'''Password and/or username do not match. Check your account details and try again.
                  ''', category='danger')

    return render_template('login.html', form=form)
                           

