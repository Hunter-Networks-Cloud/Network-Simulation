from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange



class RegistrationForm(FlaskForm):
    nodes = IntegerField('Number of Nodes',
                           validators=[DataRequired(), NumberRange(min=0, max=10)])
    basestations = IntegerField('Number of Base Stations',
                        validators=[DataRequired(), NumberRange(min=0, max=10)])
    submit = SubmitField('Simulate')
