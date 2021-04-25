from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddForm(FlaskForm):
    job = EmailField('Job', validators=[DataRequired()])
    leader = PasswordField('Team Leader', validators=[DataRequired()])
    size = EmailField('Work Size', validators=[DataRequired()])
    collaborators = PasswordField('Collaborators', validators=[DataRequired()])
    finished = BooleanField('Is finished?')
    sub = SubmitField('Submit')