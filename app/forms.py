from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Regexp


class ContactForm(FlaskForm):
    __tablename__ = "contactuser"
    name = StringField("Name", validators=[DataRequired()])
    phone_number = StringField(
        "Contact",
        validators=[
            DataRequired(),
            Length(min=10, max=10),
            Regexp(regex="^[+-]?[0-9]$"),
        ],
    )
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    comment = TextAreaField("Remarks (if any)")
    submit = SubmitField("Submit")
