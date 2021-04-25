from flask import Flask, render_template, url_for, redirect, make_response, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.jobs import Jobs
from data.users import User
from requests import get
from data import users_api
import requests

db_session.global_init("db/mars_explorer.sqlite")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/users_show/<int:user_id>')
def addep(user_id):
    user = get(f'http://localhost:8080/api/users/{user_id}').json()
    req = requests.get(f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={user['users']['city_from']}&format=json")
    if req:
        js = req.json()
        top = js["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        coor = ','.join(top["Point"]["pos"].split())
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={coor}&spn=0.03,0.03&l=sat"
        print(map_request)
        city_map = requests.get(map_request)
        map_file = "static/img/map" + str(user_id) + ".png"
        with open(map_file, "wb") as file:
            file.write(city_map.content)
    else:
        print("ERROR")
    return render_template('user_nost.html', title='Nostalgy', f=user["users"], mp=map_file)


if __name__ == '__main__':
    app.register_blueprint(users_api.blueprint)
    app.run(port=8080, host='127.0.0.1')