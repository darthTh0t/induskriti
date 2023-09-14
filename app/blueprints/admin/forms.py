# Admin Related Forms

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class GalleryForm(FlaskForm):
    image = FileField(validators=[
        FileAllowed(['jpg', 'png', 'jpeg'], "Please upload images only"),
        FileRequired()
    ])
    submit_btn = SubmitField("Upload")