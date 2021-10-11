from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email, EqualTo, Regexp
from flask_wtf.recaptcha import validators

import re

# TODO: adapt jinja template to new classes
class AccessForm(FlaskForm):
    """
    Defines common properties and variables.
    Defines common fields.
    """

    # Define common properties
    passwordRe = re.compile(
        "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
    )
    failed_pwrd_validation_msg = "Your password must contain at least 8 characters, at least one UPPER case letter, one lower case letter, one number and one special character"

    min_pwrd_len = 8
    min_usr_len = 5
    max_usr_len = 20

    # Define common fields
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=min_pwrd_len),
            Regexp(
                passwordRe,
                flags=0,
                message=failed_pwrd_validation_msg,
            ),
        ],
    )


class RegistrationForm(AccessForm):
    # TODO: Not all the fiels from AccessForm are needed here.
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=AccessForm.min_usr_len, max=AccessForm.max_usr_len),
        ],
    )

    passwordConfirmation = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            Length(min=AccessForm.min_pwrd_len),
            EqualTo(
                AccessForm.password
            ),  # TODO: check if this works. It isn't a string.
        ],
    )
    submit = SubmitField("Sign Up")


class LoginForm(AccessForm):
    # TODO: Not all the fiels from AccessForm are needed here.

    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
