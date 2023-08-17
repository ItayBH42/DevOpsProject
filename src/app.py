from flask import Flask
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your root password'
app.config['MYSQL_DB'] = 'flask'
app.config["SECRET_KEY"] = '143c90cfbf76cb0b91d59813c9f128c6'
mysql = MySQL(app)
bcrypt = Bcrypt(app)
import src.routes
