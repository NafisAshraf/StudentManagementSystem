from flask import Flask

from dotenv import load_dotenv
import os
import MySQLdb


app = Flask(__name__)
load_dotenv()


# connection = MySQLdb.connect(
#   host= os.getenv("HOST"),
#   user=os.getenv("USERNAME"),
#   passwd= os.getenv("PASSWORD"),
#   db= os.getenv("DATABASE"),
#   autocommit = True,
#   ssl_mode = "VERIFY_IDENTITY"
#   ssl      = {
#     "ca": "/etc/ssl/cert.pem"
#   }
# )



import mysql.connector as sql

connection = sql.connect(host="aws.connect.psdb.cloud",
                   database="mydb",
                   user="bo1sifju3j4baqiwvd1z",
                   password="pscale_pw_fiVes8i7umh1GKl979nh0kgopinsnYGfifwngf9PUhr",
                    )



@app.route('/')
def index():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return data

if __name__ == '__main__':
    app.run(debug=True)