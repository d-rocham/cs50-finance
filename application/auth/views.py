from flask import render_template, request, flash, session, url_for
from werkzeug.utils import redirect

from . import auth

from ..models import Users

from .forms import LoginForm, RegistrationForm

from flask_login import login_user, login_required, logout_user


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # Forget any user_id
    # session.clear() TODO: understand this session.clear. Is it necessary w. Gringberg's instructions?

    if request.method == "POST":
        if form.validate_on_submit():  # If form validation succesful
            user = Users.query.filter_by(email=form.email.data).first()

            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember.data)
                next = request.args.get("next")

                if next is None or next.startswith("/"):
                    next = url_for("main.index")

                return redirect(next)

            """ flash(f"Loged in as {form.email.data}!", "success")
            return apology("LOGGED IN!") """
            # Session.clear() prevents apology to work.

        return render_template("auth/login.html", form=form)

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("auth/login.html", form=form)


@auth.route("/register", methods=["GET", "POST"])
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
            return flash("DONE")
            # redirect(url_for("index")) TODO: once database is implemented, do redirecto to index.
        else:
            return render_template("auth/register.html", form=form)
            # TODO: what to do if form validation fails?

        # TODO: If user is already logged in, alert() that he already has an account, redirect to index
    else:
        return render_template("auth/register.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    """Log user out"""
    logout_user()

    return redirect(url_for("main.index"))
