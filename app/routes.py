# File: app/routes.py

from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User

#
# FIX: Create the Blueprint object here, before defining any routes.
#
bp = Blueprint('routes', __name__)


@bp.route('/')
@bp.route('/home')
@login_required
def home():
    """Home page for logged-in users."""
    return render_template('home.html', title='Home')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('routes.login'))

        login_user(user, remember=True)
        return redirect(url_for('routes.home'))

    return render_template('login.html', title='Log In')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """Handle new user registration."""
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash('Username and password are required!', 'warning')
            return redirect(url_for('routes.register'))

        if User.query.filter_by(username=username).first():
            flash('This username is already taken. Please choose another.', 'warning')
            return redirect(url_for('routes.register'))

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash('Congratulations, you are now a registered user! Please log in.', 'success')
        return redirect(url_for('routes.login'))

    return render_template('register.html', title='Register')


@bp.route('/logout')
@login_required
def logout():
    """Log the user out."""
    logout_user()
    return redirect(url_for('routes.login'))