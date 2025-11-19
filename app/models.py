from app import db,login_manager,bcrypt
from flask_login import UserMixin
from datetime import datetime

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String,nullable=True)
    email=db.Column(db.String,nullable=True)
    periodo=db.Column(db.DateTime,default=datetime.now())
    senha=db.Column(db.String,nullable=True)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.senha, password)


    