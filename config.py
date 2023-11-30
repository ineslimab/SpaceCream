import pymysql
import logging
from flask import Flask, render_template
from flask import jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'app'
app.config['MYSQL_DATABASE_PASSWORD'] = '123'
app.config['MYSQL_DATABASE_DB'] = 'db'
app.config['MYSQL_DATABASE_HOST'] = 'db'

app.secret_key = 'SESSION_SECRET_KEY'

mysql.init_app(app)

logging.basicConfig(level=logging.DEBUG)