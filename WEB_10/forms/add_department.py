from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddDepForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    chief = IntegerField('Chief', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    members = StringField('Members')
    sub = SubmitField('Submit')