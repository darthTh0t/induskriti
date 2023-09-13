from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ContactForm(FlaskForm):
    """Contact Form"""

    name = StringField("Name", validators=[DataRequired()])
    phone_number = StringField(
        "Contact No.",
        validators=[DataRequired(), Length(min=10, max=14)],
    )
    email = StringField(
        "Email Address",
        validators=[DataRequired(), Email(message=("Not a valid email address"))],
    )
    comment = TextAreaField("Remarks (if any)")
    # recaptcha = RecaptchaField()
    # date = HiddenField()
    submit = SubmitField("Submit")





# Admin Related Forms

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class GalleryForm(FlaskForm):
    image = FileField(FileAllowed(['jpg', 'png', 'jpeg'], "Please upload Images Only"), validators=[FileRequired()])
    submit_btn = SubmitField("Upload")

class BlogForm(FlaskForm):
    blog_title = StringField('Blog Title', validators=[DataRequired(), Length(min=5, max=30)])
    blog_body = TextAreaField('Please enter the blog text', validators=[DataRequired(), Length(min=100)])
    blog_submit = SubmitField('Publish your Blog')