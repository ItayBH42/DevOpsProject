from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\mgpro\\Devops_project\\DevOpsProject\\trial.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

import src.routes

