import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

#Metodos para conección a base de datos y autenticación


#Metodo para saber desde otras vistas si un usuario está autenticado
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

#Metodo para que se retorne la sección de usuario en cada request. 
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()



#Rutas para vistas


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """ Metodo para registrar usuarios en la app gateway """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter_by(username=username).first() is not None:
            error = 'User {} is already registered.'.format(username)

        if error is None:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()            
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        """ Metodo para loguin de usuarios en la app web gateway """
        username = request.form['username']
        password = request.form['password']
        error = None
        user = User.query.filter_by(username=username,password=password).first()

        if user is None:
            error = 'Incorrect username or password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    """Metodo para logout de usuario"""
    session.clear()
    return redirect(url_for('index'))