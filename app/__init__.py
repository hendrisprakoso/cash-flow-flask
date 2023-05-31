from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_pyfile('config.py')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cash_flow'

mysql = MySQL(app)


from app.endpoints.users import usersController