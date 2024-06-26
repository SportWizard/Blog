from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Blog_credentials
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["GET", "POST"])
def setup():
    #check if blog_credentials also exists (meaning a blog is already made)
    if not Blog_credentials.query.first():
        if request.method == "POST":
            blog_name = request.form.get("blog_name")
            password = request.form.get("password")

            blog_credentials = Blog_credentials(blog_name=blog_name, password=generate_password_hash(password, method='pbkdf2:sha256')) #create a model (sort of like creating an object from a class)
            db.session.add(blog_credentials)
            db.session.commit()

            return redirect(url_for("blog.blog_page"))

        return render_template("setup.html")
    else:
        return redirect(url_for("blog.blog_page"))

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")

        admin = Blog_credentials.query.first()

        if check_password_hash(admin.password, password):
            login_user(admin)

            return redirect(url_for("blog_writer.blog_writer_page"))

    return render_template("login.html")