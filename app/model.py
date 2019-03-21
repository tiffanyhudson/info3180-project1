from . import db

class UserProfile(db.Model):
    
    __tablename__= 'user_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(80))
    last_name= db.Column(db.String(80))
    gender= db.Column(db.String(80))
    email= db.Column(db.String(80))
    location=db.Column(db.String(80))
    biography=db.Column(db.String(2000))
    profile_picture=db.Column(db.String(100))
    
    def _init_ (self, first_name, last_name, gender, email, location, biography, profile_picture):
        self.first_name = first_name 
        self.last_name = last_name 
        self.gender = gender 
        self.email = email 
        self.location = location 
        self.biography = biography 
        self.profile_picture = profile_picture
        
    def is_authenticated(self):
        return True
        
    def is_active(self):
        return True
        
    def is_anonymous(self):
        return False
        
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
                    
    def _repr_(self):
        return '<User %r>' % (self.username)