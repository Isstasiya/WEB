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


pr = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
        'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
k = {
    "title": 'Анкета',
    "surname": "Watny",
    "name": "Mark",
    "education": "выше среднего",
    "profession": "штурман марсохода",
    "sex": "male",
    "motivation": "Всегда мечтал застрять на Марсе",
    "ready": "True"
}


@app.route('/<tit>')
@app.route('/index/<tit>')
def sl(tit):
    return render_template('base.html', title=tit)

@app.route('/training/<prof>')
def train(prof):
    return render_template('prof.html', prof=prof)

@app.route('/list_prof/<lit>')
def lis(lit):
    return render_template('listb.html', lt=lit, prof=pr)

@app.route('/answer')
@app.route('/auto_answer')
def ans():
    return render_template('answer.html', **k)

@app.route("/login", methods=['GET', 'POST'])
def lg():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')