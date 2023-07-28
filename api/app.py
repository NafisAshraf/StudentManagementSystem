from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length
import pymysql
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

app.config['SECRET_KEY'] = "skey"

db_host = os.getenv("HOST")
db_user = os.getenv("USER")
db_password = os.getenv("PASSWORD")
db_name = os.getenv("DATABASE")

def get_db_connection():
    return pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        ssl={
            "ca": "cacert.pem"
        }
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/database')
def database():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students;")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('database.html', students=data)

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        city = request.form['city']

        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students (name, phone, email, city) VALUES (%s, %s, %s, %s)",
            (name, phone, email, city)
        )
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('database'))

    return render_template('add_student.html')

@app.route('/remove_student', methods=['GET', 'POST'])
def remove_student():
    if request.method == 'POST':
        student_id = request.form['student_id']
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('database'))
    else:
        return render_template('remove_student.html')



class LoginForm(FlaskForm):
    email = StringField('Email Adress', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=20)])


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        # print("Hello World")
        # return f" Username: {form.email.data} Password: {form.password.data} "
        return redirect(url_for('index'))

    return render_template('form.html', form=form)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)
