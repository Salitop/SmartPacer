import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base




# Cria a engine para se conectar ao banco de dados
engine = sqlalchemy.create_engine('mysql://root:ZvFRi8OvrgkD8zUW2IzH@containers-us-west-153.railway.app:5839/railway')

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()



# Cria a base declarativa
Base = declarative_base()

# Cria a classe da tabela Usuario
class Usuario(Base):
    __tablename__ = 'Usuario'
    IdUsuario = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    Nome = sqlalchemy.Column(sqlalchemy.String(50))
    Senha = sqlalchemy.Column(sqlalchemy.String(20))
    Login = sqlalchemy.Column(sqlalchemy.String(20))


# Tabela Equipe
class Equipe(Base):
    __tablename__ = 'Equipe'
    IdEquipe = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    NomeEquipe = sqlalchemy.Column(sqlalchemy.String(20), nullable=False)


# Tabela Sprint
class Sprint(Base):
    __tablename__ = 'Sprint'
    IdSprint = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    Ano = sqlalchemy.Column(sqlalchemy.SmallInteger, nullable=False)
    Semestre = sqlalchemy.Column(sqlalchemy.SmallInteger, nullable=False)
    Descricao = sqlalchemy.Column(sqlalchemy.String(20))
    Ativo = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)


# Tabela EquipeSprint
class EquipeSprint(Base):
    __tablename__ = 'EquipeSprint'
    IdEquipeSprint = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    IdEquipe = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Equipe.IdEquipe'), nullable=False)
    IdSprint = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Sprint.IdSprint'), nullable=False)
    PontosPacer = sqlalchemy.Column(sqlalchemy.SmallInteger)


# Tabela UsuarioEquipe
class UsuarioEquipe(Base):
    __tablename__ = 'UsuarioEquipe'
    IdUsuarioEquipe = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    UsuarioId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Usuario.IdUsuario'), nullable=False)
    EquipeId = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Equipe.IdEquipe'), nullable=False)


# Cria a classe da tabela UsuarioPacer
class UsuarioPacer(Base):
    __tablename__ = 'UsuarioPacer'
    IdUsuarioPacer = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    IdUsuario = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Usuario.IdUsuario'), nullable=False)
    IdUsuarioAvaliado = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Usuario.IdUsuario'), nullable=False)
    IdSprint = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Sprint.IdSprint'), nullable=False)
    NotaP = sqlalchemy.Column(sqlalchemy.SmallInteger)
    NotaA = sqlalchemy.Column(sqlalchemy.SmallInteger)
    NotaC = sqlalchemy.Column(sqlalchemy.SmallInteger)
    NotaER = sqlalchemy.Column(sqlalchemy.SmallInteger)

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)
