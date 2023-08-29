from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, data_required

class SignupFrom(FlaskForm):
    Name = StringField(label="Enter name", validators=[Length(min=2, max=30)])
    Email = StringField(label="Enter email address")
    Password = PasswordField(label="Enter password", validators=[Length(min=6)])
    PasswordRe = PasswordField(label="Re-enter password", validators=[EqualTo('Password')])
    Submit = SubmitField(label="Signup")



class LoginForm(FlaskForm):
    Email = StringField(label="Email")
    Password = PasswordField(label="Password")
    Submit = SubmitField(label="Login")
