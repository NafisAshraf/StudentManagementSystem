from flask import Flask
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()



app = Flask(__name__)

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_name = os.getenv("DATABASE")

print(db_host, db_user, db_password, db_name)

@app.route('/')
def index():
    connection = pymysql.connect(host=db_host,
                    user=db_user,
                    password=db_password,
                    database=db_name,
                    # ssl_mode="VERIFY_IDENTITY",
                    ssl={
                        "ca": "/etc/ssl/cert.pem"
                    }
                    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return str(data)

if __name__ == '__main__':
    app.run(debug=True)



