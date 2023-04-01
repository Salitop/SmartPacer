from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class Usuario(db.Model):
    __tablename__ = "Usuario"
    idUsuario = db.Column(db.Integer, primary_key=True,nullable=False)
    nome = db.Column(db.String(50))
    senha = db.Column(db.String(20))
    login = db.Column(db.String(20))


# Tabela Equipe
class Equipe(db.Model):
    __tablename__ = 'Equipe'
    IdEquipe = db.Column(db.Integer, primary_key=True, nullable=False)
    NomeEquipe = db.Column(db.String(20), nullable=False)


# Tabela Sprint
class Sprint(db.Model):
    __tablename__ = 'Sprint'
    IdSprint = db.Column(db.Integer, primary_key=True, nullable=False)
    Ano = db.Column(db.SmallInteger, nullable=False)
    Semestre = db.Column(db.SmallInteger, nullable=False)
    Descricao = db.Column(db.String(20))
    Ativo = db.Column(db.Boolean, nullable=False)


# Tabela EquipeSprint
class EquipeSprint(db.Model):
    __tablename__ = 'EquipeSprint'
    IdEquipeSprint = db.Column(db.Integer, primary_key=True, nullable=False)
    IdEquipe = db.Column(db.Integer, db.ForeignKey('Equipe.IdEquipe'), nullable=False)
    IdSprint = db.Column(db.Integer, db.ForeignKey('Sprint.IdSprint'), nullable=False)
    PontosPacer = db.Column(db.SmallInteger)


# Tabela UsuarioEquipe
class UsuarioEquipe(db.Model):
    __tablename__ = 'UsuarioEquipe'
    IdUsuarioEquipe = db.Column(db.Integer, primary_key=True, nullable=False)
    UsuarioId = db.Column(db.Integer, db.ForeignKey('Usuario.idUsuario'), nullable=False)
    EquipeId = db.Column(db.Integer, db.ForeignKey('Equipe.IdEquipe'), nullable=False)


# Cria a classe da tabela UsuarioPacer
class UsuarioPacer(db.Model):
    __tablename__ = 'UsuarioPacer'
    IdUsuarioPacer = db.Column(db.Integer, primary_key=True, nullable=False)
    IdUsuario = db.Column(db.Integer, db.ForeignKey('Usuario.idUsuario'), nullable=False)
    IdUsuarioAvaliado = db.Column(db.Integer, db.ForeignKey('Usuario.idUsuario'), nullable=False)
    IdSprint = db.Column(db.Integer, db.ForeignKey('Sprint.IdSprint'), nullable=False)
    NotaP = db.Column(db.SmallInteger)
    NotaA = db.Column(db.SmallInteger)
    NotaC = db.Column(db.SmallInteger)
    NotaER = db.Column(db.SmallInteger)
