# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Cars(db.Model):
    __tablename__ = 'Cars'
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String(length=80), nullable=False)
    make = db.Column(db.String(length=255), nullable=False)
    model = db.Column(db.String(length=80), nullable=False)
    colour = db.Column(db.String(length=80), nullable=False)
    year = db.Column(db.String(length=120), nullable=False)
    transmision = db.Column(db.String(length=200), nullable=False)
    car_type = db.Column(db.String(length=80), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    photo = db.Column(db.String(length=80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)

    
    def __init__(self,discription,make,model,colour,year,transmision,car_type,price,photo,user_id):
        self.discription = discription
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmision = transmision
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = user_id

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

    def __repr__(self):
        return '<Cars %r>' % self.id
    
class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('Cars.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    
    def __init__(self,car_id,user_id):
        self.car_id = car_id
        self.user_id = user_id
    
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

    def __repr__(self):
        return '<Favourites %r>' % self.user_id
    
class Users(db.Model):
    __tablename__= 'Users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=80), nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    name = db.Column(db.String(length=80), nullable=False)
    email = db.Column(db.String(length=80), nullable=False)
    location = db.Column(db.String(length=80), nullable=False)
    biography = db.Column(db.String(length=255), nullable=False)
    photo = db.Column(db.String(length=80), nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False)

    def __init__(self,username,password,name,email,location,biography,photo,date_joined):
        self.username = username
        self.set_password = generate_password_hash(password, method='pbkdf2:sha256')
        self.name = name
        self.email = email
        self.location = location
        self.biography = biography
        self.photo = photo
        self.date_joined = date_joined
    
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

    def __repr__(self):
        return '<Users %r>' % self.username