from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, render_template, url_for, redirect, make_response, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.jobs import Jobs
from data.users import User
from requests import get
from data import users_resource
import requests

db_session.global_init("db/mars_explorer.sqlite")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)

if __name__ == '__main__':
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')
    api.add_resource(users_resource.UsersListResource, '/api/v2/users/') 
    app.run(port=8080, host='127.0.0.1')