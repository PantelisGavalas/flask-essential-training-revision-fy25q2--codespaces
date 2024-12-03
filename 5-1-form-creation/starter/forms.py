from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

'''
*** StringField --> a field for text input. Generates an HTML input element of type text.
*** SubmitField --> a field for submit button. Generates an HTML input element of type submit.
'''
class MyForm(FlaskForm):
  name = StringField('Name')
  submit = SubmitField('Submit')
  