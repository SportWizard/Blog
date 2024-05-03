from flask import Blueprint, render_template, request
from flask_login import logout_user
from . import db
from .models import Blog_credentials, Post, Comment

blog = Blueprint("blog", __name__)

@blog.route("/blog", methods=["GET", "POST"])
def blog_page(): #the function cannot be the same name as the blueprint
    logout_user()

    if request.method == "POST":
        comment = request.form.get("comment")
        post_id = request.form.get("postId")

        if comment:
            comment = Comment(context=comment, post_id=post_id)
            db.session.add(comment)
            db.session.commit()

    return render_template("blog.html", blog_credentials=Blog_credentials.query.first(), posts=Post.query.all(), comments=Comment.query.all())