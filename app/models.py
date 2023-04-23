import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base




# Cria a engine para se conectar ao banco de dados
# engine = sqlalchemy.create_engine('mysql://root:ZvFRi8OvrgkD8zUW2IzH@containers-us-west-153.railway.app:5839/railway')
engine = sqlalchemy.create_engine("mysql+mysqldb://root:password@localhost:3306/SmartPacer")

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

# Adicionando Alunos
usuario1 = Usuario(Nome='Hariel Thums', Senha='123456', Login='HT')
usuario2 = Usuario(Nome='Guilherme Garcia', Senha='123456', Login='GG')
usuario3 = Usuario(Nome='Vinicius Oliveira', Senha='123456', Login='VO')
usuario4 = Usuario(Nome='Eduarda Giudice', Senha='123456', Login='EG')
usuario5 = Usuario(Nome='Bárbara Bidettí', Senha='123456', Login='BB')
usuario6 = Usuario(Nome='Juliany', Login='J', Senha='123456')
usuario7 = Usuario(Nome='André Silva', Login='AS', Senha='123456')
usuario8 = Usuario(Nome='Igor', Login='I', Senha='123456')
usuario9 = Usuario(Nome='Thomas Palma', Login='TP', Senha='123456')
usuario10 = Usuario(Nome='Pedro Willian', Login='PW', Senha='123456')
usuario11 = Usuario(Nome='Elias', Login='E', Senha='123456')
usuario12 = Usuario(Nome='Leonardo Ribeiro', Login='LR', Senha='123456')
usuario13 = Usuario(Nome='Sarah Montana', Login='SM', Senha='123456')
usuario14 = Usuario(Nome='Rita Ferreira', Login='RF', Senha='123456')
usuario15 = Usuario(Nome='Raul Inglesias', Login='RI', Senha='123456')
usuario16 = Usuario(Nome='Jonathan Assis', Login='JA', Senha='123456')
usuario17 = Usuario(Nome='Luiz Miguel', Login='LM', Senha='123456')
usuario18 = Usuario(Nome='Edryan Matheus', Login='EM', Senha='123456')
usuario19 = Usuario(Nome='Ana Clara', Login='AC', Senha='123456')
usuario20 = Usuario(Nome='Israel Augusto', Login='IA', Senha='123456')

# Adicionando Equipes
equipe1 = Equipe(NomeEquipe='Cluster8')
equipe2 = Equipe(NomeEquipe='Moneymind')
equipe3 = Equipe(NomeEquipe='Nox')
equipe4 = Equipe(NomeEquipe='SmartPacer')

# Adicionando Sprints
sprint1 = Sprint(Ano=2023, Semestre=1, Descricao='Sprint 1', Ativo=True)
sprint2 = Sprint(Ano=2023, Semestre=1, Descricao='Sprint 2', Ativo=True)
sprint3 = Sprint(Ano=2023, Semestre=1, Descricao='Sprint 3', Ativo=True)
sprint4 = Sprint(Ano=2023, Semestre=1, Descricao='Sprint 4', Ativo=True)
sprint5 = Sprint(Ano=2023, Semestre=2, Descricao='Sprint 1', Ativo=False)
sprint6 = Sprint(Ano=2023, Semestre=2, Descricao='Sprint 2', Ativo=False)
sprint7 = Sprint(Ano=2023, Semestre=2, Descricao='Sprint 3', Ativo=False)
sprint8 = Sprint(Ano=2023, Semestre=2, Descricao='Sprint 4', Ativo=False)

# # Criando 5 inserts aleatórios na tabela EquipeSprint
# equipe_sprint1 = EquipeSprint(IdEquipe=1, IdSprint=1, PontosPacer=20)
# equipe_sprint2 = EquipeSprint(IdEquipe=2, IdSprint=2, PontosPacer=15)
# equipe_sprint3 = EquipeSprint(IdEquipe=3, IdSprint=3, PontosPacer=30)
# equipe_sprint4 = EquipeSprint(IdEquipe=4, IdSprint=4, PontosPacer=5)
# equipe_sprint5 = EquipeSprint(IdEquipe=5, IdSprint=5, PontosPacer=25)

session.add_all([usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10, usuario11, usuario12, usuario13, usuario14, usuario15, usuario16, usuario17, usuario18, usuario19, usuario20])
session.commit()
session.add_all([sprint1, sprint2, sprint3, sprint4, sprint5, sprint6, sprint7, sprint8])
session.commit()
session.add_all([equipe1, equipe2, equipe3, equipe4])
session.commit()
# session.add_all([equipe_sprint1, equipe_sprint2, equipe_sprint3, equipe_sprint4, equipe_sprint5])
# session.commit()
session.add(UsuarioEquipe(UsuarioId=1, EquipeId=1))
session.add(UsuarioEquipe(UsuarioId=2, EquipeId=1))
session.add(UsuarioEquipe(UsuarioId=3, EquipeId=1))
session.add(UsuarioEquipe(UsuarioId=4, EquipeId=1))
session.add(UsuarioEquipe(UsuarioId=5, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=6, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=7, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=8, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=9, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=10, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=11, EquipeId=2))
session.add(UsuarioEquipe(UsuarioId=12, EquipeId=3))
session.add(UsuarioEquipe(UsuarioId=13, EquipeId=3))
session.add(UsuarioEquipe(UsuarioId=14, EquipeId=3))
session.add(UsuarioEquipe(UsuarioId=15, EquipeId=3))
session.add(UsuarioEquipe(UsuarioId=16, EquipeId=3))
session.add(UsuarioEquipe(UsuarioId=17, EquipeId=4))
session.add(UsuarioEquipe(UsuarioId=18, EquipeId=4))
session.add(UsuarioEquipe(UsuarioId=19, EquipeId=4))
session.add(UsuarioEquipe(UsuarioId=20, EquipeId=4))
session.commit()

# # João avalia Maria na Sprint 1
# up1 = UsuarioPacer(IdUsuario=1, IdUsuarioAvaliado=2, IdSprint=1, NotaP=2, NotaA=3, NotaC=1, NotaER=0)
# session.add(up1)

# # Maria avalia Pedro na Sprint 1
# up2 = UsuarioPacer(IdUsuario=2, IdUsuarioAvaliado=3, IdSprint=1, NotaP=1, NotaA=2, NotaC=3, NotaER=0)
# session.add(up2)

# # Pedro avalia Ana na Sprint 1
# up3 = UsuarioPacer(IdUsuario=3, IdUsuarioAvaliado=4, IdSprint=1, NotaP=3, NotaA=2, NotaC=1, NotaER=3)
# session.add(up3)

# # Ana avalia Lucas na Sprint 2
# up4 = UsuarioPacer(IdUsuario=4, IdUsuarioAvaliado=6, IdSprint=2, NotaP=2, NotaA=1, NotaC=2, NotaER=1)
# session.add(up4)

# # Lucas avalia Fernanda na Sprint 2
# up5 = UsuarioPacer(IdUsuario=6, IdUsuarioAvaliado=7, IdSprint=2, NotaP=3, NotaA=3, NotaC=2, NotaER=0)
# session.add(up5)

# # Fernanda avalia João na Sprint 2
# up6 = UsuarioPacer(IdUsuario=7, IdUsuarioAvaliado=1, IdSprint=2, NotaP=1, NotaA=2, NotaC=3, NotaER=1)
# session.add(up6)

# # Juliana avalia Rafael na Sprint 3
# up7 = UsuarioPacer(IdUsuario=8, IdUsuarioAvaliado=9, IdSprint=3, NotaP=2, NotaA=2, NotaC=2, NotaER=3)
# session.add(up7)

# # Rafael avalia Laura na Sprint 3
# up8 = UsuarioPacer(IdUsuario=9, IdUsuarioAvaliado=10, IdSprint=3, NotaP=3, NotaA=3, NotaC=1, NotaER=2)
# session.add(up8)

# # Laura avalia Carlos na Sprint 3
# up9 = UsuarioPacer(IdUsuario=10, IdUsuarioAvaliado=5, IdSprint=3, NotaP=1, NotaA=1, NotaC=3, NotaER=2)
# session.add(up9)

# # Carlos avalia Ana na Sprint 3
# up10 = UsuarioPacer(IdUsuario=5, IdUsuarioAvaliado=4, IdSprint=3, NotaP=2, NotaA=1, NotaC=3, NotaER=0)
# session.add(up10)




# # # # Executando a sessão para inserir os registros no banco de dados
# session.commit()



