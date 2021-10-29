import os
from flask.helpers import url_for

from flask_sqlalchemy import SQLAlchemy

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from sqlalchemy.orm import backref

from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from forms import RegistrationForm, LoginForm

# Configure application
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "9d7daea4a862dd6513fee22b8223ad73"

# Ensure responses aren't cached
@app.after_request  # TO UNDERSTAND: what does this decorator do? Why is it needed (it comes from CS50 staff)
def after_request(response):
    """
    TO UNDERSTAND: Why are these headers being changed?
    TO UNDERSTAND: What is "Cache-Control", "Expires", Pragma"?
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response  # TO UNDERSTAND: Who receives the response back?


# Custom filter
app.jinja_env.filters["usd"] = usd  # TO UNDERSTAND: How does this work?

# Configure session to use filesystem (instead of signed cookies) #TODO: Come back to this when Corey's tutorial reachies user authentication & Sessions
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Open database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Make sure API key is set
""" if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set") """

db = SQLAlchemy(app)


class Users(db.Model):
    # Table columns
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwrd_hash = db.Column(db.String(60), nullable=False)
    cash = db.Column(db.Float, nullable=False, default=10000.00)

    # Table relations
    owned_stock = db.relationship("OwnedStock", backref="owner", lazy=True)
    user_transactions = db.relationship("Transactions", backref="user", lazy=True)

    def __repr__(self):
        return f"Users('{self.username}', '{self.email}' with '{self.cash}')"


class OwnedStock(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    stock_symbol = db.Column(db.String(8), nullable=False)
    cost_on_purchase = db.Column(db.Float, nullable=False)
    num_of_shares = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"OwnedStock('{self.user_id}', '{self.stock_symbol}', '{self.cost_on_purchase}', '{self.num_of_shares}')"


class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )
    stock_symbol = db.Column(db.String(8), nullable=False)
    action = db.Column(db.String(8), nullable=False)
    affected_number = db.Column(db.Integer, nullable=False)
    cost_on_action = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Transactions('{self.user_id}', '{self.stock_symbol}', '{self.action}', '{self.affected_number}', '{self.cost_on_action}', '{self.date}')"


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
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


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    return apology("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


"""
TO UNDERSTAND: what is e? Where does it come from?
"""


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


"""
TO UNDERSTAND: How does this loop work? 
TO UNDERSTAND: When is it called? 
TO UNDERSTAND: Whie does "errorhandler" take 2 arguments?
"""
# Listen for errors
for code in default_exceptions:  # TO UNDERSTAND: What is default_exceptions made of?
    app.errorhandler(code)(
        errorhandler
    )  # TO UNDERSTAND: Where does errorhandler come from?
