from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    user = StringField(
        'Name',
        [DataRequired()]
    )
    number = StringField(
        'Email',
        [DataRequired()]
    )
    submit = SubmitField('Submit')
