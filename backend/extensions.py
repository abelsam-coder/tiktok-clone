from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
bcrypt = Bcrypt()
def create_api(app):
       return Api(app)
