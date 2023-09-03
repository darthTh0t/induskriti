from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, PasswordField
from wtforms.validators import DataRequired, Email, Length, Regexp


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
    file_upload = FileField(validators=[
            Regexp(
                r'^[^/\\]\.(jpg|jpeg|png|gif)$',
                message="Invalid image file format. Please upload a valid image file."
            )])
    submit_btn = SubmitField("Upload")