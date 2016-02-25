from flask import session, render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from .. import db
from ..models import User, Contacts
from .forms import LoginForm, RegistrationForm
from functools import wraps
from app import login_manager

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('main.login'))
	return wrap

@auth.route('/')
@auth.route('/home')
def home():
	return render_template('home.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print "catedgrfkng ske"
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            session['logged_in'] = True
            return redirect(request.args.get('next') or url_for('auth.home'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))



@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # get the user rcontacts default
        #user_contacts = Contacts.query.filter_by(username='User').first()
        user = User(username=form.username.data,
                    password=form.password.data,
                    
                    email =form.email.data,
                    PhoneNum =form.PhoneNum.data
                    )
        #user.relContacts = user_contacts
        db.session.add(user)
        db.session.commit()
        flash('Welcome to your Contacts Manager! \n Please login to continue.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/addnew/', methods=['GET', 'POST'])
def addContact():
	form = AddNewContactForm()
	if form.validate_on_submit():

		return redirect(url_for('home'))

	return render_template('addnew.html', 
                           title='Add New',
                           form=form,
                           )






