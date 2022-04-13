# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField ('description',validators=[DataRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','png','Images only!'])])