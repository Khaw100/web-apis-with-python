from flask import Flask, jsonify, render_template
import json
# Intitialise the app
app = Flask(__name__)

# Functions
def readJSON(filename='data.json'):
    with open(filename,'r') as read_file:
        data = json.load(read_file)
        return data

# Define what the app does
@app.get("/")
def index():
    return render_template('index.html')

@app.get("/mahasiswa")
def mahasiswa():
    data = readJSON()
    return jsonify(data)

@app.get("/bismillahsukses")
def bismillah():
    response = {"string" : "bismillah TST A aamiiin"}
    return jsonify(response)