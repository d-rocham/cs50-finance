from flask import flash, redirect, render_template, request, session, url_for
from flask_login import login_required

# ATTENTION: Remember that, within a blueprint, Flask applies a namespace to all the endpoints of a blueprint.
# Hence,`url_for` must be used as `url_for(main.<desired url>)` or as `url_for(.<desired url>)`

from . import main
from .forms import RegistrationForm, LoginForm
from .. import db
from ..models import Users, OwnedStock, Transactions
from .helpers import apology, login_required, lookup, usd

# TODO: usd is used as a custom jinja filter. Relocate.

""" from application.models import Users, OwnedStock, Transactions
from application.helpers import apology, login_required, lookup, usd
from application.forms import RegistrationForm, LoginForm
 """

# Ensure responses aren't cached
@main.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@main.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@main.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    return apology("TODO")


@main.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@main.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    return apology("TODO")


@main.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
