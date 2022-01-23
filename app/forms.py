from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    TimeField,
    TextAreaField,
    BooleanField,
    SubmitField
)
from wtforms.validators import DataRequired
from wtforms.widgets import DateInput, TimeInput


class AppointmentForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    start_date = DateField('Start date', [DataRequired()], widget=DateInput())
    start_time = TimeField('Start time', [DataRequired()], widget=TimeInput())
    end_date = DateField('End date', [DataRequired()], widget=DateInput())
    end_time = TimeField('End time', [DataRequired()], widget=TimeInput())
    description = TextAreaField('Description', [DataRequired()])
    private = BooleanField('Private?')
    submit = SubmitField('Create an appointment')
