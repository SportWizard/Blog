from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import Post

blog_writer = Blueprint("blog_writer", __name__)

@blog_writer.route("/blog-writer", methods=["GET", "POST"])
def blog_writer_page():
    if request.method == "POST":
        title = request.form.get("title")
        context = request.form.get("context")

        if not title or not context:
            flash("Title or Context can't be empty.", category="error")
        else:
            post = Post(title=title, context=context)

            db.session.add(post)
            db.session.commit()

            flash("Post created", category="success")

            return redirect(url_for("blog.blog_page"))

    return render_template("blogWriter.html")