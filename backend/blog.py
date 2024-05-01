from flask import Blueprint, render_template
from .models import Blog_credentials
from . import db

blog = Blueprint("blog", __name__)

@blog.route("/blog")
def blog_page():
    return render_template("blog.html", blog_credentials=Blog_credentials.query.first())