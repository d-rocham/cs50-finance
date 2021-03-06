""" Application package constructor """

""" TODO: Check if all these imports are necessary. Why must I import render_template here? 
Are the exceptions really used here? etc...
"""

from flask import Flask, flash, redirect, render_template, request, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import backref
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from config import config

db = SQLAlchemy()
session = Session()


def create_app(config_name):
    """Application factory function"""
    app = Flask(__name__)
    # Retrieve configuration from class in config dictionary
    app.config.from_object(config[config_name])
    # Call staticmethod  init_app from Config class on app
    config[config_name].init_app(app)

    # Initialize extensions
    db.init_app(app)
    session.init_app(app)

    # register blueprint

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    # Return application instance
    return app
