from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length

class ContactForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired()])
  subject = StringField('Subject', validators=[DataRequired(), Length(max=20)])
  message = StringField('Message', widget=TextArea(), validators=[DataRequired()])
  terms = BooleanField(validators=[DataRequired()])
  submit = SubmitField('Submit')