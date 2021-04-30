import os

from flask import Flask
from flask import request
from werkzeug.security import generate_password_hash
from flask.helpers import flash
from flask import abort, redirect, url_for
import re
from email_validator import validate_email, EmailNotValidError


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db as dbInterface

    @app.route('/register', methods=['POST', 'GET'])
    def register():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        db = dbInterface.get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif email:
            try:
                validate_email(email)
            except EmailNotValidError as e:
                error = 'Email is incorrect. ' + str(e)
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {} is already registered.'.format(username)
        elif db.execute(
            'SELECT id FROM user WHERE email = ?', (email,)
        ).fetchone() is not None:
            error = 'User with email {} is already registered.'.format(email)

        if error is None:
            db.execute(
                'INSERT INTO user (username, email, password) VALUES (?, ?, ?)',
                (username, email, generate_password_hash(password))
            )
            db.commit()
            return redirect("https://psych-game.github.io/thank-you.html")
        else:
            flash(error)
            return "<h1>"+error+"</h1>"

    dbInterface.init_app(app)

    return app