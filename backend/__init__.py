from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("KEY")

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #template_folder is used if folder "template" is not in the same folder as this file
    app = Flask("Blog", template_folder="./frontend/templates", static_folder="./frontend/static")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SECRET_KEY"] = key #this is used for flash (to output whether something is success or error
    db.init_app(app)

    #inside this function, so no loop import between different files
    from .auth import auth #from relative directory (same directory/package) import auth <- can be either a variable or a function that is public
    from .blog import blog
    from .blog_writer import blog_writer

    #blueprint from blog and blog_writer
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(blog, url_prefix="/")
    app.register_blueprint(blog_writer, url_prefix="/")

    create_database(app)

    return app

def create_database(app):
    with app.app_context(): #creates a Flask application context, which allows you to access the application context-aware variables such as current_app and g within the function
        db.create_all() #SQLAlchemy function creates all the tables defined in your application's models. It inspects the models and generates the necessary SQL to create the corresponding database tables
        print("Created database")