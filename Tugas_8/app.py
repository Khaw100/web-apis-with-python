from flask import Flask, make_response, jsonify, request, render_template, redirect
import json
from flask_mysqldb import MySQL
from login import *
import jwt
import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tubes_tst'

app.config['SECRET_KEY'] = 'gfseeker'

mysql = MySQL(app)

@app.get("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute(f'select * from job_skills order by Location desc limit 5')
    data = cur.fetchall()
    return render_template('index.html', data =data)

@app.route("/create", methods = ['GET', 'POST'])
def create():
    cur = mysql.connection.cursor()
    company_name = request.values.get('company')
    title = request.values.get('title')
    category = request.values.get('category')
    location = request.values.get('location')
    resp = request.values.get('responsibilities')
    min_qual = request.values.get('min_qual')
    pref_qual = request.values.get('pref_qual')
    query = f"INSERT INTO job_skills VALUES ('{company_name}', '{title}', '{category}', '{location}', '{resp}', '{min_qual}', '{pref_qual}', 'Available')"
    cur.execute(query)
    print(query)
    mysql.connection.commit()
    return render_template('create.html')

@app.route("/delete", methods = ['GET', 'POST','DELETE'])
def delete():
    cur = mysql.connection.cursor()
    title = request.values.get('title')
    location = request.values.get('location')
    query = f"DELETE FROM job_skills WHERE Title = '{title}' AND  Location = '{location}'"
    cur.execute(query)
    print(query)
    mysql.connection.commit()
    return render_template('delete.html')
    

@app.route("/update", methods = ['GET', 'POST', 'PUT'])
def update():
    cur = mysql.connection.cursor()
    avail = request.values.get('avail')
    title = request.values.get('title')
    location = request.values.get('location')
    query = f"UPDATE job_skills SET Availability = '{avail}' WHERE Title = '{title}' AND  Location = '{location}'"
    cur.execute(query)
    print(query)
    mysql.connection.commit()
    return render_template('update.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.values.get('username')
    password = request.values.get('password')
    if validation(username, password):
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return render_template('login.html')
    else:
        return 'Username atau Password salah'