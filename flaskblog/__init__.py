from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_mail import Mail
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dc5a09978edc11c02c8d90b8a0957736'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True 
app.config['MAIL_USERNAME'] = '__YOUR USERNAME__'
app.config['MAIL_PASSWORD'] = '__YOUR__PASSWORD__'

mail = Mail(app)

from flaskblog.users.routes import users 
app.register_blueprint(users)

from flaskblog.post.routes import posts 
app.register_blueprint(posts)

from flaskblog.users.routes import main 
app.register_blueprint(main)


