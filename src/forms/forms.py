from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, email_validator, DataRequired

class SignupFrom(FlaskForm):
    Name = StringField(label="Enter name", validators=[DataRequired(), Length(min=2, max=30)])
    Email = StringField(label="Enter email address", validators=[DataRequired(), Email()])
    Password = PasswordField(label="Enter password", validators=[DataRequired(), Length(min=6)])
    PasswordRe = PasswordField(label="Re-enter password", validators=[DataRequired(), EqualTo('Password')])
    Submit = SubmitField(label="Signup")



class LoginForm(FlaskForm):
    Email = StringField(label="Email")
    Password = PasswordField(label="Password")
    Submit = SubmitField(label="Login")
