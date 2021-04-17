from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    job = StringField('Job', validators=[DataRequired()])
    team_leader = IntegerField('Team Leader', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = StringField('Collaborators')
    haz = IntegerField('Hazard category')
    is_finished = BooleanField('Is finished?')
    sub = SubmitField('Submit')