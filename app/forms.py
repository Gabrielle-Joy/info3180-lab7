from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired, DataRequired, Email, length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('First Name', validators=[DataRequired()])
    photo = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])

