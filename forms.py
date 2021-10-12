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
    Defines failed validation messages
    """

    # Length limits, password RegEx

    passwordRe = re.compile(
        "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
    )

    min_pwrd_len = 8
    min_usr_len = 5
    max_usr_len = 20

    # Failed validation messages for each field
    failed_validation_messages = {
        "password": f"Your password must have at least one UPPER case letter, one lower case letter, one number and one special character",
        "username": f"Your username should be between {min_usr_len} and {max_usr_len} characters long",
        "email": "Please provide a valid email address",
        "password_confirmation": "The passwords do not match",
    }

    # Define common fields
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(message=failed_validation_messages["email"])],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=min_pwrd_len),
            Regexp(
                passwordRe,
                flags=0,
                message=failed_validation_messages["password"],
            ),
        ],
    )


class RegistrationForm(AccessForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(
                min=AccessForm.min_usr_len,
                max=AccessForm.max_usr_len,
                message=AccessForm.failed_validation_messages["username"],
            ),
        ],
    )

    passwordConfirmation = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            Length(
                min=AccessForm.min_pwrd_len,
                message=AccessForm.failed_validation_messages["password"],
            ),
            EqualTo(
                "password",
                message=AccessForm.failed_validation_messages["password_confirmation"],
            ),
        ],
    )
    submit = SubmitField("Sign Up")


class LoginForm(AccessForm):

    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


# TODO: Change password field.
