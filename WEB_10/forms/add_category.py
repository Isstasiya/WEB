from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, IntegerField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddCatForm(FlaskForm):
    name = StringField('Category', validators=[DataRequired()])
    sub = SubmitField('Submit')