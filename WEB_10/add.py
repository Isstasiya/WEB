from flask import Flask, render_template, url_for, redirect, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, login_required, logout_user
from data import db_session
from data.jobs import Jobs
from data.users import User
from data.login import LoginForm
from data.add_job import AddForm

db_session.global_init("db/mars_explorer.sqlite")
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
def index():
    db_sess = db_session.create_session()
    j = db_sess.query(Jobs).all()
    return render_template("works.html", j=j)

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

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')