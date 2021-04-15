from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astro_id = StringField('id астронавта', validators=[DataRequired()])
    astro_ps = PasswordField('Пароль астронавта', validators=[DataRequired()])
    comm_id = StringField('id капитана', validators=[DataRequired()])
    comm_ps = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

pr = ["Ридли Скотт", "Энди Уир", "Марк Уотни", "Венката Капур", "Тедди Сандерс", "Шон Бин"]


@app.route('/distribution')
def train():
    return render_template('distribution.html', austr=pr)


@app.route('/table/<sex>/<int:age>')
def tab(sex, age):
    return render_template('table.html', s=sex, a=age)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')