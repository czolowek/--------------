from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    tours = db.relationship('Tour', secondary='user_tours', backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def is_validate_password(self, password):
        return check_password_hash(self.password_hash, password)

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    departure = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

user_tours = db.Table('user_tours',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('tour_id', db.Integer, db.ForeignKey('tour.id'), primary_key=True)
)