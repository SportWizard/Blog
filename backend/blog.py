from flask import Blueprint, render_template
from .models import Blog_credentials, Post

blog = Blueprint("blog", __name__)

@blog.route("/blog")
def blog_page(): #the function cannot be the same name as the blueprint
    return render_template("blog.html", blog_credentials=Blog_credentials.query.first(), posts=Post.query.all())