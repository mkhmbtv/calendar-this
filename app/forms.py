from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    TimeField,
    TextAreaField,
    BooleanField,
    SubmitField
)
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import DateInput, TimeInput
from datetime import datetime


class AppointmentForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    start_date = DateField('Start date', [DataRequired()], widget=DateInput())
    start_time = TimeField('Start time', [DataRequired()], widget=TimeInput())
    end_date = DateField('End date', [DataRequired()], widget=DateInput())
    end_time = TimeField('End time', [DataRequired()], widget=TimeInput())
    description = TextAreaField('Description', [DataRequired()])
    private = BooleanField('Private?')
    submit = SubmitField('Create an appointment')

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(field.data, form.end_time.data)
        if form.start_date.data != field.data:
            msg = 'End date and start date must be the same'
            raise ValidationError(msg)
        elif start >= end:
            msg = 'End date/time must come after start date/time'
            raise ValidationError(msg)
