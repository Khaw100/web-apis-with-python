from flask import Flask, jsonify, render_template, request
import json
# Intitialise the app
app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
# Functions
def readJSON(filename='data.json'):
    with open(filename,'r') as read_file:
        data = json.load(read_file)
        return data

def writeJSONPerson(person, status, nim, filename='data.json'):
    with open(filename,"r+") as file:
        json_file = json.load(file)
        json_file[person]["Status"] = status
        json_file[person]["NIM"] = nim
        file.seek(0)
        json.dump(json_file,file,indent=4)
        file.truncate()


# Define what the app does
@app.get("/")
def index():
    return render_template('index.html')

@app.get("/mahasiswa")
def mahasiswa():
    data = readJSON()
    return jsonify(data)

# @app.get("/bismillahsukses")
# def bismillah():
#     response = {"string" : "bismillah TST A aamiiin"}
#     return jsonify(response)

@app.get("/write")
def edit():
    name = request.args.get("name")
    status = request.args.get("status")
    nim = request.args.get("nim")
    data = readJSON()
    pstatus = data[name]["Status"]
    pnim = data[name]["NIM"]
    if not status and not nim and name:
        return jsonify({"status":"error"})
    elif not status and nim and name:
        writeJSONPerson(name,pstatus,nim)
    elif status and not nim and name:
        writeJSONPerson(name,status,pnim)     
    else:
        writeJSONPerson(name,status,nim)
    data = readJSON()
    return jsonify(data)

@app.get("/changestatus")
def changeStatus():
    return render_template('submit.html')

@app.get("/a")
def tes():
    data = readJSON()
    return data["Rakha"]