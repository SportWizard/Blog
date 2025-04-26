from flask_login import UserMixin #used for login
from sqlalchemy.sql import func
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
    comment = db.relationship("Comment", backref="post")
    date_create = db.Column(db.DateTime(timezone=True), default=func.now())

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    context = db.Column(db.String(100), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))