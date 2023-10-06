from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

class ResponseForm(FlaskForm):
    speed = FloatField('speed', validators=[DataRequired()], render_kw={"placeholder": "Enter speed", "autofocus": True})