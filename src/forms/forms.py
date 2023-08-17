from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignupFrom(FlaskForm):
    Name = StringField(label="Enter name")
    Email = StringField(label="Enter email address")
    Password = PasswordField(label="Enter password")
    PasswordRe = PasswordField(label="Re-enter password")
    Submit = SubmitField(label="Signup")


class LoginForm(FlaskForm):
    Email = StringField(label="Email")
    Password = PasswordField(label="Password")
    Submit = SubmitField(label="Login")
