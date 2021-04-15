from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.user import RegisterForm


db_session.global_init("db/mars_explorer.sqlite")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.submit():
        if form.password.data != form.password_again.data:
            return render_template('reg.html', title='Регистрация',
                                   form=form,
                                   message="Password mismatch")
        try:
            k = int(form.age.data)
        except Exception as s:
            return render_template('reg.html', title='Регистрация',
                                   form=form,
                                   message="Invalid type in age string")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('reg.html', title='Регистрация',
                                   form=form,
                                   message="This user already exists")
        user = User(
            name=form.name.data,
            email=form.email.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('reg.html', title='Регистрация', form=form)

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')