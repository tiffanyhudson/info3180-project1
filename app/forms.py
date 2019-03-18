from flask_wtf import FlaskForm

from wtforms import StringField, SelectField, FileField, TextAreaField

from wtforms.validators import DataRequired, Email, FileRequired , FileAllowed

class ProfileForm(FlaskForm):

    firstname = StringField('first_name', validators=[DataRequired()])
    
    lastname = StringField('last_name', validators=[DataRequired])
    
    email= StringField('Email', validators=[DataRequired(), Email()])
    
    location= StringField('location', validators=[DataRequired()])
    
    gender= SelectField('gender', choices=[('M','Male'),('F','Female')])

    biography = TextAreaField('biography', validators=[DataRequired()])
    
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])