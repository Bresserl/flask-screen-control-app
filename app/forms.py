from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, Email


class File_upload_form(FlaskForm):
    file = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload')


class Video_upload_form(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    url = StringField('URL: ', validators=[DataRequired()])
    submit = SubmitField('Upload')


class Text_upload_form(FlaskForm):
    title = StringField('Title: ', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Upload')

class Login_form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Stay signed in')
    submit = SubmitField('Login')
