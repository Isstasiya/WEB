from flask import Flask, render_template, url_for, redirect, make_response, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.jobs import Jobs
from data.users import User
from forms.login import LoginForm
from forms.add_job import AddForm
from forms.login import LoginForm
from forms.user import RegisterForm

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

@app.route("/")
def index():
    db_sess = db_session.create_session()
    j = db_sess.query(Jobs).all()
    return render_template("works.html", j=j)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect("/")
        return render_template('log.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('log.html', title='Авторизация', form=form)

@app.route('/add_job', methods=['GET', 'POST'])
def addj():
    form = AddForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            team_leader=form.team_leader.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Adding a job', form=form)

@app.route('/change_job/<int:id>', methods=['GET', 'POST'])
def changej(id):
    form = AddForm()
    db_sess = db_session.create_session()
    jb = db_sess.query(Jobs).filter(Jobs.id == id, ((Jobs.team_leader == current_user.id) | (current_user.id == 1))).first()
    if request.method == "GET":
        if jb:
            form.job.data=jb.job
            form.work_size.data=jb.work_size
            form.collaborators.data=jb.collaborators
            form.team_leader.data=jb.team_leader
            form.is_finished.data=jb.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        jb.job=form.job.data
        jb.work_size=form.work_size.data
        jb.collaborators=form.collaborators.data
        jb.team_leader=form.team_leader.data
        jb.is_finished=form.is_finished.data
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Changing a job', form=form)

@app.route('/delete_job/<int:id>', methods=['GET', 'POST'])
@login_required
def deletej(id):
    db_sess = db_session.create_session()
    jb = db_sess.query(Jobs).filter(Jobs.id == id, Jobs.team_leader == current_user.id).first()
    if jb:
        db_sess.delete(jb)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')