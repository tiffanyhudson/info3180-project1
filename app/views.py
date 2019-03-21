"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
#from app.forms import LoginForm
from app.model import UserProfile 
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename
from app.forms import profile 
import psycopg2 
import random 
import os
from datetime import datetime


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')



@app.route('/profile',methods=['POST', 'GET'])
def Addprofile(): 
    form=profile()
    if request.method=='POST' and form.validate_on_submit():
        
        #id=random.randint(1,100000)
        Name=request.form['first_name']
        LastName=request.form['last_name']
        Gender=request.form['gender']
        Email=request.form['email']
        Location=request.form['location']
        Biography=request.form['biography']
        #ppn=request.form['ProfilePicture']
        ProfilePicture=form.photo.data 
        
        #file = request.files['Profile Pictures']
        filename=secure_filename(ProfilePicture.filename)
        ProfilePicture.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
         
        user = UserProfile(Name,LastName,Gender,Email,Location,Biography,filename)
        db.session.add(user)
        db.session.commit()
        flash('You have been sucessfully added') 
        return redirect(url_for('Users'))
            
        
    return render_template('profile.html',form=profile)     
    
@app.route('/profiles') 
def Users(): 
    users=db.session.query(UserProfile).all()
    return render_template('profiles.html',users=users)

@app.route('/profiles/<userid>')
def fullprofile(userid):
    user=UserProfile.query.get(userid)
    #user=users[userid]
    return render_template('profilepage.html',user=user)
    
    
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")



def format_date_joined(day, month, year):
    b=datetime(year, month, day)
    return b.strftime("%B, %Y")
