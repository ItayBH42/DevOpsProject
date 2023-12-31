import bcrypt
import sqlite3
import re

from src.app import app,bcrypt
from flask import render_template, redirect, g, url_for, flash
from ..forms.forms import SignupFrom, LoginForm

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('trial.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.route('/users')
def getUsers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template("users.html", users=users)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupFrom()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        db = get_db()
        password = bcrypt.generate_password_hash(form.Password.data).decode("utf8")
        res = db.execute("insert into users (username,email,user_password)"
                            "values(?,?,?)", (form.Name.data, form.Email.data, password))
        db.commit()
        return redirect(url_for("login"))
    return render_template("signup_form.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db = get_db()  # Get the SQLite database connection
        email = form.Email.data

        # Fetch user data from the database using a parameterized query
        cur = db.cursor()
        cur.execute("SELECT * FROM users WHERE email=?", (email,))
        userAttempt = cur.fetchone()

        if userAttempt and bcrypt.check_password_hash(userAttempt[3], form.Password.data):
            # You might want to store user data in the session or use a proper user management system
            user_data = {"id": userAttempt[0], "name": userAttempt[1], "email": userAttempt[2]}
            # Redirect to home page after successful login
            return redirect(url_for(""))  # 'home' is the name of the home route
        else:
            print("Wrong email or password")
            return render_template("login.html", form=form)  # Return the login form with a message

    return render_template("login.html", form=form)




#         # if (form.Password.data != form.PasswordRe.data):
#         #     validation=False
#         #     print(form.Password.data)

#         #     regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#         #     def isValid(email):
#         #         if re.fullmatch(regex, form.Email.data):
#         #             print("Valid email")
#         #         else:
#         #             print("Invalid email")
#         #     flash("invalid email adress")
#         #     validation=False
#         #     print(form.Email.data)
#         # if validation: