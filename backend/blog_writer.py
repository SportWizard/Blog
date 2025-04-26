from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from werkzeug.security import generate_password_hash
from . import db
from .models import Blog_credentials, Post

blog_writer = Blueprint("blog_writer", __name__)

@blog_writer.route("/blog-writer", methods=["GET", "POST"])
@login_required
def blog_writer_page():
    if request.method == "POST":
        title = request.form.get("title")
        context = request.form.get("context")

        #check if title or context is not empty
        if title and context:
            post = Post.query.filter_by(title=title).first()

            #check if a post with similar title already exist
            if post:
                post.context = context
            else:
                #create new post if it doesn't exist
                post = Post(title=title, context=context)
                db.session.add(post)

            db.session.commit()

            return redirect(url_for("blog.blog_page"))

        post_title = request.form.get("postTitle")

        #check if the input is not empty
        if post_title:
            delete_post = Post.query.filter_by(title=post_title).first()

            #check if the post exists
            if delete_post:
                db.session.delete(delete_post)
                db.session.commit()

            return redirect(url_for("blog.blog_page"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirmPassword")

        if password and confirm_password:
            admin = Blog_credentials.query.first()

            if password == confirm_password:
                admin.password = generate_password_hash(password, method='pbkdf2:sha256')

                db.session.commit()

                return redirect(url_for("blog.blog_page"))

        blog_name = request.form.get("blogName")

        if blog_name:
            admin = Blog_credentials.query.first()

            admin.blog_name = blog_name

            db.session.commit()

            return redirect(url_for("blog.blog_page"))

    return render_template("blogWriter.html")