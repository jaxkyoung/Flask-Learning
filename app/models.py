from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# user table, to track current registered users that have been approved
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    fName = db.Column(db.String(20), nullable = False)
    sName = db.Column(db.String(30), nullable = False)
    userType = db.Column(db.String(20), nullable = False)

# pending user table, to track pending users waiting for access approval
class PendingUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)
    fName = db.Column(db.String(20), nullable = False)
    sName = db.Column(db.String(30), nullable = False)
    userType = db.Column(db.String(20), nullable = False)
    
# comment table to track comments on questions from question tabel
# foreign keys linking to question and users
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cBody = db.Column(db.String(2000))
    postDate = db.Column(db.DateTime)
    posterId = db.Column(db.Integer, db.ForeignKey(User.id))
