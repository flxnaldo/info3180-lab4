from flask_wtf import FlaskForm
from flask import Flask
from werkzeug.utils import secure_filename
from flask_wtf.file import FileRequired, FileField, FileAllowed

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])