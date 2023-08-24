import bcrypt
import sqlite3

from src.app import app
from flask import render_template, redirect, g
from ..forms.forms import SignupFrom, LoginForm
from src.app import bcrypt

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('C:/Users/mgpro/Devops_project/DevOpsProject/trial.db')
        g.db.row_factory = sqlite3.Row
    return g.db

app.config['DATABASE'] = 'C:/Users/mgpro/Devops_project/DevOpsProject/trial.db'

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
        db = get_db()
        password = bcrypt.generate_password_hash(form.Password.data).decode("utf8")
        res = db.execute("insert into users (username,email,user_password)"
                          "values(?,?,?)", (form.Name.data, form.Email.data, password))
        db.commit()

        if res == 1:
            return redirect(url_for("login"))

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
