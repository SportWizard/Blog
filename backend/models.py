from flask_login import UserMixin #used for login
from . import db

#models for sqlalchemy
class Blog_credentials(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    context = db.Column(db.String(-1), nullable=False) #unlimited length