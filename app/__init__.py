from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .views import views
from .models import models

def create_app():
 app = Flask(__name__)
 app.config['SECRET_KEY']='ADJDFJFDHGSJGJSDJGDHJG'
 
 db = SQLAlchemy(app)
 login_manager = LoginManager(app)


 app.register_blueprint(views,url_prefix='/')
 app.register_blueprint(models,url_prefix='/')

 return app