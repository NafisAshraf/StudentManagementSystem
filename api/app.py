from flask import Flask
import mysql.connector as sql
import os
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_name = os.getenv("DATABASE")





@app.route('/')
def index():
    connection = sql.connect(host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name
                    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return data

if __name__ == '__main__':
    app.run(debug=True)



