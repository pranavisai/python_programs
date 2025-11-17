from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, URL


class ETForm(FlaskForm):
    name = StringField(
        "Cafe Name",
        validators=[DataRequired()]
    )
    location = StringField(
        "Cafe Location on Google Maps(URL)",
        validators=[DataRequired(), URL()]
    )
    open_time = StringField(
        "Opening Time e.g. 8AM",
        validators=[DataRequired(), Length(max=20)]
    )
    close_time = StringField(
        "Closing Time e.g. 5:30PM",
        validators=[DataRequired(), Length(max=20)]
    )
    coffee = SelectField(
        "Coffee Rating",
        choices=["☕️", "☕️☕️", "☕️☕️☕️" , "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
        validators=[DataRequired()]
    )

    wifi = SelectField(
        "Wifi Strength Rating",
        choices=["✖", "🛜", "🛜🛜", "🛜🛜🛜", "🛜🛜🛜🛜", "🛜🛜🛜🛜🛜"],
        validators=[DataRequired()]
    )

    power = SelectField(
        "Power Socket Availability",
        choices=["✖", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )

    submit = SubmitField("Submit")
