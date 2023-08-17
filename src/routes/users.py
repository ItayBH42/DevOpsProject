import bcrypt

from src.app import app, mysql
from flask import render_template, redirect
from ..forms.forms import SignupFrom, LoginForm
from src.app import bcrypt


@app.route('/users')
def getUsers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template("users.html", users=users)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupFrom()
    if form.validate_on_submit():
        cur = mysql.connection.cursor()
        password = bcrypt.generate_password_hash(form.password.data).decode("utf8")
        res = cur.execute("insert into users (name,email,password)"
                          "values(%s,%s,%s)", (form.name.data, form.email.data, password))
        cur.connection.commit()

        if res == 1:
            return redirect("/login")

    return render_template("signup_form.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # print(form.email.data)
        cur = mysql.connection.cursor()

        res = cur.execute(f"select * from users where email='{form.email.data}'")
        if res == 1:
            userAttempt = cur.fetchall()[0]

            if bcrypt.check_password_hash(userAttempt[3], form.password.data):
                user["data"] = {"id": userAttempt[0], "name": userAttempt[1], "email": userAttempt[2],
                                "password": userAttempt[3]}
                return redirect("/")
            else:
                print("wrong password")
    return render_template("login.html", form=form)
