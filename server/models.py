from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class User(db.Model):
    __tablename__ = "users"
    idUsuario = db.Column(db.Integer, primary_key=True,nullable=False)
    nome = db.Column(db.String(50))
    senha = db.Column(db.String(20))
    login = db.Column(db.String(20))