from . import db

#models for sqlalchemy
class Blog_credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(150), nullable=False)