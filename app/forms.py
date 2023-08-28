from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, Email, Length


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


class ReviewForm(FlaskForm):
    """Testimonial/Review Form"""

    name = StringField("Name", validators=[DataRequired()])
    remark = TextAreaField("Your Feedback", validators=[DataRequired()])
