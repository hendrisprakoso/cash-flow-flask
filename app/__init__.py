from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL(app)


from app.endpoints.users import (usersController)
from app.endpoints.transaction import (transactionsController)
from app.endpoints.report import (reportTransactionController)