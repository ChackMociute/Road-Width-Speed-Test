from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AssessmentForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    code = StringField('title', validators=[DataRequired()])