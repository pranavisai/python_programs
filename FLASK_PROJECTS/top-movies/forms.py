from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, URL


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")