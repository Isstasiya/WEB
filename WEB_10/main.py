from flask import Flask, render_template, url_for, redirect, make_response, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data import db_session
from data.jobs import Jobs
from data.users import User
from data.departments import Department
from data.category import Category
from forms.login import LoginForm
from forms.add_job import AddForm
from forms.login import LoginForm
from forms.user import RegisterForm
from forms.add_department import AddDepForm
from forms.add_category import AddCatForm

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

@app.route("/departments")
def depart():
    db_sess = db_session.create_session()
    j = db_sess.query(Department).all()
    return render_template("departments.html", j=j)

@app.route("/categories")
def categ():
    db_sess = db_session.create_session()
    j = db_sess.query(Category).all()
    return render_template("categories.html", j=j)

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
            haz_categ=form.haz.data,
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
            form.haz.data=jb.haz_categ
        else:
            abort(404)
    if form.validate_on_submit():
        jb.job=form.job.data
        jb.work_size=form.work_size.data
        jb.collaborators=form.collaborators.data
        jb.team_leader=form.team_leader.data
        jb.haz_categ=form.haz.data
        jb.is_finished=form.is_finished.data
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Changing a job', form=form)

@app.route('/delete_job/<int:id>', methods=['GET', 'POST'])
@login_required
def deletej(id):
    db_sess = db_session.create_session()
    jb = db_sess.query(Jobs).filter(Jobs.id == id, ((Jobs.team_leader == current_user.id) | (current_user.id == 1))).first()
    if jb:
        db_sess.delete(jb)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')

@app.route('/add_department', methods=['GET', 'POST'])
def addep():
    form = AddDepForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dp = Department(
            title=form.title.data,
            chief=form.chief.data,
            members=form.members.data,
            email=form.email.data
        )
        db_sess.add(dp)
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_departments.html', title='Adding a department', form=form)

@app.route('/change_department/<int:id>', methods=['GET', 'POST'])
def changeep(id):
    form = AddDepForm()
    db_sess = db_session.create_session()
    dp = db_sess.query(Department).filter(Department.id == id, ((Department.chief == current_user.id) | (current_user.id == 1))).first()
    if request.method == "GET":
        if dp:
            form.title.data=dp.title
            form.chief.data=dp.chief
            form.members.data=dp.members
            form.email.data=dp.email
        else:
            abort(404)
    if form.validate_on_submit():
        dp.title=form.title.data
        dp.chief=form.chief.data
        dp.members=form.members.data
        dp.email=form.email.data
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_departments.html', title='Changing a department', form=form)

@app.route('/delete_department/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteep(id):
    db_sess = db_session.create_session()
    dp = db_sess.query(Department).filter(Department.id == id, ((Department.chief == current_user.id) | (current_user.id == 1))).first()
    if dp:
        db_sess.delete(dp)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')

@app.route('/add_category', methods=['GET', 'POST'])
def addcat():
    form = AddCatForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dp = Category(
            name=form.name.data
        )
        db_sess.add(dp)
        db_sess.commit()
        return redirect('/categories')
    return render_template('add_category.html', title='Adding a category', form=form)

@app.route('/change_category/<int:id>', methods=['GET', 'POST'])
def changecat(id):
    form = AddCatForm()
    db_sess = db_session.create_session()
    dp = db_sess.query(Category).filter(Category.id == id, (current_user.id == 1)).first()
    if request.method == "GET":
        if dp:
            form.name.data=dp.name
        else:
            abort(404)
    if form.validate_on_submit():
        dp.name=form.name.data
        db_sess.commit()
        return redirect('/categories')
    return render_template('add_category.html', title='Changing a category', form=form)

@app.route('/delete_category/<int:id>', methods=['GET', 'POST'])
@login_required
def deletecat(id):
    db_sess = db_session.create_session()
    dp = db_sess.query(Category).filter(Category.id == id, (current_user.id == 1)).first()
    if dp:
        db_sess.delete(dp)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/categories')

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')