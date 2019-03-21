from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Request(FlaskForm):

    item_name = StringField("Item Name")
    description = StringField("Description")
    submit = SubmitField("Submit")
