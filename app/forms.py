from flask import render_template, request, redirect, url_for, flash 
from flask_wtf import FlaskForm 
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email

class profile(FlaskForm):

    firstname = StringField('first_name', validators=[DataRequired()])
    
    lastname = StringField('last_name', validators=[DataRequired])
    
    email= StringField('Email', validators=[DataRequired(), Email()])
    
    location= StringField('location', validators=[DataRequired()])
    
    gender= SelectField('gender', choices=[('M','Male'),('F','Female')])

    biography = TextAreaField('biography', validators=[DataRequired()])
    
    photo = FileField('Photo', validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])