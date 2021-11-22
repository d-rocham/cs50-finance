from flask import flash, redirect, render_template, request, session, url_for

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


@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # Forget any user_id
    session.clear()

    if request.method == "POST":
        if form.validate_on_submit():  # If form validation succesful
            flash(f"Loged in as {form.email.data}!", "success")
            return apology("LOGGED IN!")
            # Session.clear() prevents apology to work.
        else:
            return render_template("login.html", form=form)

        # ATTENTION: Commented-out block below should be removed after form validation and form failure are tested
        """ if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403) """

        # ATTENTION: Commented-out block below will be replaced with respective library.
        """ # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/") """

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", form=form)


@main.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@main.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    form = RegistrationForm()

    if request.method == "POST":
        if form.validate_on_submit():
            # TODO: store credentials in database
            flash(
                f"Account created for {form.username.data} with email {form.email.data}!",
                "success",
            )
            return apology("DONE")
            # redirect(url_for("index")) TODO: once database is implemented, do redirecto to index.
        else:
            return render_template("register.html", form=form)
            # TODO: what to do if form validation fails?

        # TODO: If user is already logged in, alert() that he already has an account, redirect to index
    else:
        return render_template("register.html", form=form)


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

    """
 def errorhandler(e):
    #Handle error
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler) """
