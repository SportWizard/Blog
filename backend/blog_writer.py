from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from . import db
from .models import Post

blog_writer = Blueprint("blog_writer", __name__)

@blog_writer.route("/blog-writer", methods=["GET", "POST"])
@login_required
def blog_writer_page():
    if request.method == "POST":
        title = request.form.get("title")
        context = request.form.get("context")

        #check if title or context is not empty
        if title and context:
            post = Post(title=title, context=context)

            db.session.add(post)
            db.session.commit()

            return redirect(url_for("blog.blog_page"))

        post_title = request.form.get("postTitle")

        #if two posts have the same title, it will delete the oldest one
        delete_post = Post.query.filter_by(title=post_title).first()

        #check if the post exist and if delete_post is not empty
        if post_title and delete_post:
            db.session.delete(delete_post)
            db.session.commit()

            return redirect(url_for("blog.blog_page"))

    return render_template("blogWriter.html")