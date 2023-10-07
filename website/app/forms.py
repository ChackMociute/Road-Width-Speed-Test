from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import DataRequired

class ParticipantForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()], render_kw={"placeholder": "Enter your name or identifier"})

class ResponseForm(FlaskForm):
    speed = FloatField('speed', validators=[DataRequired()], render_kw={"placeholder": "Enter speed", "autofocus": True})