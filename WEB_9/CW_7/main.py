from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data import db_session
from data.jobs import Jobs
from data.users import User


db_session.global_init("db/mars_explorer.sqlite")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def sl():
    ss = db_session.create_session()
    j = ss.query(Jobs).all()
    return render_template("works.html", j=j)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')