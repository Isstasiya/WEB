from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/galery', methods=["GET", "POST"])
def gal():
    pic = os.listdir('static/img/peizash')
    if request.method == 'GET':
        return render_template('galery.html', pic=pic, title="Galery", n=len(pic))
    elif request.method == 'POST':
        print('ss')
        f = request.files['file']
        print('ss')
        with open(f'static/img/peizash/{len(pic) + 1}.jpg', 'wb') as fl:
            print('ss')
            fl.write(f.read())
        return redirect('/galery')


@app.route('/member')
def mem():
    with open("templates/members.json", "r", encoding="utf8") as f:
        mn = json.loads(f.read())
    return render_template('member.html', members=mn)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')