from flask import Flask, jsonify, request, render_template
import json
from flask_mysqldb import MySQL

# Initialise the app
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tubes_tst'

# mydb = mysql.connector.connect(
#     host="localhost",
#     username="root",
#     password="",
#     database="testtst"
# )

mysql = MySQL(app)

@app.get("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute(f'select * from job_skills')
    data = cur.fetchall()
    return render_template('index.html',data = data)
