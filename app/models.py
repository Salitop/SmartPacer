import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base




# Cria a engine para se conectar ao banco de dados
# engine = sqlalchemy.create_engine('mysql://root:ZvFRi8OvrgkD8zUW2IzH@containers-us-west-153.railway.app:5839/railway')
engine = sqlalchemy.create_engine("mysql+mysqldb://root:@localhost:3306/SmartPacer")

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

# # Criando 5 inserts aleatórios
# # usuario1 = Usuario(Nome='João', Senha='123456', Login='joao123')
# # usuario2 = Usuario(Nome='Maria', Senha='abc123', Login='maria456')
# # usuario3 = Usuario(Nome='Pedro', Senha='senha123', Login='pedro789')
# # usuario4 = Usuario(Nome='Ana', Senha='qwe123', Login='ana456')
# # usuario5 = Usuario(Nome='Lucas', Senha='senha456', Login='lucas123')
# # usuario1 = Usuario(Nome='João', Login='joao', Senha='123')
# # usuario2 = Usuario(Nome='Maria', Login='maria', Senha='456')
# # usuario3 = Usuario(Nome='Pedro', Login='pedro', Senha='789')
# # usuario4 = Usuario(Nome='Ana', Login='ana', Senha='abc')
# # usuario5 = Usuario(Nome='Carlos', Login='carlos', Senha='def')
# # usuario6 = Usuario(Nome='Lucas', Login='lucas', Senha='ghi')
# # usuario7 = Usuario(Nome='Fernanda', Login='fernanda', Senha='jkl')
# # usuario8 = Usuario(Nome='Juliana', Login='juliana', Senha='mno')
# # usuario9 = Usuario(Nome='Rafael', Login='rafael', Senha='pqr')
# usuario10 = Usuario(Nome='Laura', Login='laura', Senha='stu')
# usuario11 = Usuario(Nome='romulo', Login='romulo12', Senha='ghi')
# usuario12 = Usuario(Nome='tonico', Login='tonico12', Senha='jkl')
# usuario13 = Usuario(Nome='Juliano', Login='Juliano13', Senha='mno')
# usuario14 = Usuario(Nome='Rafaelauro', Login='Rafaelauro13', Senha='pqr')
# usuario15 = Usuario(Nome='Laurancio', Login='Laurancio65', Senha='stu')
# # Adicionando os registros na sessão
# # equipe1 = Equipe(NomeEquipe='Equipe A')
# # equipe2 = Equipe(NomeEquipe='Equipe B')
# # equipe3 = Equipe(NomeEquipe='Equipe C')
# # equipe4 = Equipe(NomeEquipe='Equipe D')
# # equipe5 = Equipe(NomeEquipe='Equipe E')

# # sprint1 = Sprint(Ano=2022, Semestre=1, Descricao='Sprint 1', Ativo=True)
# # sprint2 = Sprint(Ano=2022, Semestre=2, Descricao='Sprint 2', Ativo=True)
# # sprint3 = Sprint(Ano=2023, Semestre=1, Descricao='Sprint 3', Ativo=True)
# # sprint4 = Sprint(Ano=2023, Semestre=2, Descricao='Sprint 4', Ativo=True)
# # sprint5 = Sprint(Ano=2024, Semestre=1, Descricao='Sprint 1', Ativo=True)

# # sprint6 = Sprint(Ano=2024, Semestre=2, Descricao='Sprint 2', Ativo=True)
# # sprint7 = Sprint(Ano=2022, Semestre=2, Descricao='Sprint 3', Ativo=True)
# # sprint8 = Sprint(Ano=2023, Semestre=1, Descricao='Sprint 4', Ativo=True)
# # sprint9 = Sprint(Ano=2024, Semestre=1, Descricao='Sprint 3', Ativo=True)
# # sprint10 = Sprint(Ano=2022, Semestre=1, Descricao='Sprint 4', Ativo=True)

# # Criando 5 inserts aleatórios na tabela EquipeSprint
# equipe_sprint1 = EquipeSprint(IdEquipe=1, IdSprint=1, PontosPacer=20)
# equipe_sprint2 = EquipeSprint(IdEquipe=2, IdSprint=2, PontosPacer=15)
# equipe_sprint3 = EquipeSprint(IdEquipe=3, IdSprint=3, PontosPacer=30)
# equipe_sprint4 = EquipeSprint(IdEquipe=4, IdSprint=4, PontosPacer=5)
# equipe_sprint5 = EquipeSprint(IdEquipe=5, IdSprint=5, PontosPacer=25)

# session.add_all([usuario11, usuario12, usuario13, usuario14, usuario15])
# session.add_all([usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10])
# session.commit()
# session.add_all([sprint1, sprint2, sprint3, sprint4, sprint5])
# session.commit()
# session.add_all([sprint6, sprint7, sprint8, sprint9, sprint10])
# session.commit()
# session.add_all([usuario1, usuario2, usuario3, usuario4, usuario5])
# session.commit()
# session.add_all([equipe1, equipe2, equipe3, equipe4, equipe5])
# session.commit()
# session.add_all([equipe_sprint1, equipe_sprint2, equipe_sprint3, equipe_sprint4, equipe_sprint5])
# session.commit()
# session.add(UsuarioEquipe(UsuarioId=1, EquipeId=1))
# session.add(UsuarioEquipe(UsuarioId=2, EquipeId=1))
# session.add(UsuarioEquipe(UsuarioId=3, EquipeId=1))
# session.add(UsuarioEquipe(UsuarioId=4, EquipeId=2))
# session.add(UsuarioEquipe(UsuarioId=5, EquipeId=2))
# session.add(UsuarioEquipe(UsuarioId=6, EquipeId=2))
# session.add(UsuarioEquipe(UsuarioId=7, EquipeId=3))
# session.add(UsuarioEquipe(UsuarioId=8, EquipeId=3))
# session.add(UsuarioEquipe(UsuarioId=9, EquipeId=3))
# session.add(UsuarioEquipe(UsuarioId=10, EquipeId=4))
# session.add(UsuarioEquipe(UsuarioId=11, EquipeId=4))
# session.add(UsuarioEquipe(UsuarioId=12, EquipeId=4))
# session.add(UsuarioEquipe(UsuarioId=13, EquipeId=5))
# session.add(UsuarioEquipe(UsuarioId=14, EquipeId=5))
# session.add(UsuarioEquipe(UsuarioId=15, EquipeId=5))
# session.commit()

# João avalia Maria na Sprint 1
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




# # # Executando a sessão para inserir os registros no banco de dados
# session.commit()



