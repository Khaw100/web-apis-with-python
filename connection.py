import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="testtst"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM job_skills LIMIT 1")
myresult = mycursor.fetchall()
print(myresult)
