from urllib import response
from flask import Flask, render_template, request,redirect, url_for, jsonify
from flask_cors import CORS
from .models import *
from flask_bcrypt import Bcrypt ## criptografa a senha do usuario
from sqlalchemy import create_engine, Column, Integer, String, func

app = Flask(__name__)
CORS(app, supports_credentials=True)
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route("/")
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route("/cadastrarNotas",methods = ['POST'])
def calcular():
    app.run()
    session = Session()

    # if request.method == "GET":
    #     return render_template('cadastrar.html')
    # else:
    data = request.get_json()
    novoPacer = UsuarioPacer(
    NotaP = data['notaP'],
    NotaA = data['notaA'],
    NotaC = data['notaC'],
    NotaER = data['notaER'],
    IdUsuario = data['usuario'],
    IdUsuarioAvaliado = data['usuarioAvaliado'],
    IdSprint = data['idSprint']
    )
   
    session.add(novoPacer)
    session.commit()
         
    return jsonify({'result':'deu certo'})

# @app.route("/calculo", methods = ['POST'])
# def calcular():

#     data = request.get_json()

#     notaASerCalculadaP = session.query(usuariopacer).filter_by(usuarioAvaliado = data['noticia'],
#                                                               idSprint = data['idSprint'])

#     qtdnotasP = 
#     totalp = Sum(notasSprintP) / qtdnotasp

#         qtdnotasA = select count(notasSprintA) where etapa = 1 
#     totalA = Sum(notasSprintA) / qtdnotasA

#         qtdnotasC = select count(notasSprintC) where etapa = 1 
#     totalC = Sum(notasSprintC) / qtdnotasC

#         qtdnotasER = select count(notasSprintER) where etapa = 1 
#     totalER = Sum(notasSprintER) / qtdnotasER

#     return render_template('tela_exibicao')

@app.route("/obterSprintSemestreAno",methods = ['GET'])
def obterSprintSemestreAno():
    

    session = Session()
    sprintsFiltradas =  session.query(Sprint).filter_by(Semestre = request.args.get('semestre'), Ano = request.args.get('ano')).all()
    
    todas_sprints = [{'idsprint':sprintFiltrada.IdSprint,'ano':sprintFiltrada.Ano,'semestre':sprintFiltrada.Semestre,'descricao':sprintFiltrada.Descricao} for sprintFiltrada in sprintsFiltradas]
         
    return jsonify(todas_sprints)

@app.route("/obterTodasEquipes",methods = ['GET'])
def obterTodasEquipes():
    session = Session()
    equipes =  session.query(Equipe).all()
    
    todas_equipes = [{'idequipe':equipe.IdEquipe,'equipe':equipe.NomeEquipe} for equipe in equipes]
         
    return jsonify(todas_equipes)

@app.route("/obterAlunosPorIdEquipe",methods = ['GET'])
def obterAlunosPorIdEquipe():
    session = Session()

    filtro = session.query(Usuario, Equipe)\
        .join(UsuarioEquipe, Usuario.IdUsuario == UsuarioEquipe.UsuarioId)\
        .join(Equipe, Equipe.IdEquipe == UsuarioEquipe.EquipeId)\
        .filter(Equipe.IdEquipe == request.args.get('idequipe')).all()

    alunos = []

    for aluno in filtro:
        alunos.append({'idusuario': aluno[0].IdUsuario, 'nome': aluno[0].Nome})
         
    return jsonify(alunos)

@app.route("/obterTodasSprints",methods = ['GET'])
def obterTodasSprints():
    session = Session()
    sprints =  session.query(Sprint).filter_by(Ativo = 1).all()
    
    todas_sprints = [{'idsprint':sprint.IdSprint,'ano':sprint.Ano,'semestre':sprint.Semestre,'descricao':sprint.Descricao} for sprint in sprints]
         
    return jsonify(todas_sprints)

#me enviara o idequipe e idsprint, devo retornar os alunos e suas notas

@app.route("/visualizarNotasEquipeSprint",methods = ['GET'])
def visualizarNotasEquipeSprint():
    session = Session()
    filtro = session.query(UsuarioPacer.IdUsuarioAvaliado,UsuarioEquipe,Usuario)\
    .join(Usuario, UsuarioPacer.IdUsuarioAvaliado == Usuario.IdUsuario)\
    .join(UsuarioEquipe, Usuario.IdUsuario == UsuarioEquipe.UsuarioId)\
    .filter(UsuarioPacer.IdSprint == request.args.get('idsprint'),\
     UsuarioEquipe.EquipeId ==request.args.get('idequipe'))\
    .distinct().all()

    print(filtro)
    notas_aluno = []
    for aluno in filtro:
        # notasAluno = session.query(UsuarioPacer).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).all()
        notasAlunoP = session.query(func.sum(UsuarioPacer.NotaP)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        qtdNotasP = session.query(func.count(UsuarioPacer.NotaP)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        totalP = notasAlunoP/qtdNotasP

        notasAlunoA = session.query(func.sum(UsuarioPacer.NotaA)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        qtdNotasA = session.query(func.count(UsuarioPacer.NotaA)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        totalA = notasAlunoA/qtdNotasA

        notasAlunoC = session.query(func.sum(UsuarioPacer.NotaC)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        qtdNotasC = session.query(func.count(UsuarioPacer.NotaC)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        totalC = notasAlunoC/qtdNotasC
        
        notasAlunoER = session.query(func.sum(UsuarioPacer.NotaER)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        qtdNotasER = session.query(func.count(UsuarioPacer.NotaER)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        totalER = notasAlunoER/qtdNotasER
        
        
        notas_aluno.append({'nomealuno':aluno.Usuario.Nome, 'mediap':totalP, 'mediaa': totalA,'mediac': totalC,'mediaer':totalER})
    return jsonify(notas_aluno)
        
## Verifica se o usuario esta logado
@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    user = Usuario.query.filter_by(idUsuario=user_id).first()
    return jsonify({
        "id": user.idUsuario,
        "nome": user.nome
    }) 

## Rota para criar um novo usuario
@app.route("/register", methods=["POST"])
def register_user():
    session = Session()
    nome = request.json["nome"]
    senha = request.json["senha"]
    login = request.json["login"]

    user_exists = Usuario.query.filter_by(nome=nome).first() is not None
    if user_exists:
        return jsonify({"error": "Usuario já existe"})

    hashed_password = bcrypt.generate_password_hash(senha)
    new_user = Usuario(nome=nome, senha=hashed_password, login=login)
    sqlalchemy.session.add(new_user)
    sqlalchemy.session.commit()

    session["user_id"] = new_user.idUsuario

    return jsonify({
        "id": new_user.idUsuario,
        "nome": new_user.nome
    })

## Rota de login
@app.route("/login", methods=["POST"] )
def login_user():
    nome = request.json["nome"]
    senha = request.json["senha"]
    

    user = Usuario.query.filter_by(nome=nome).first()
    if user is None:
        return jsonify({"error": "Não autorizado"}), 401
    
    if not bcrypt.check_password_hash(user.senha,senha):
        return jsonify({"error": "Não autorizado"}), 401
    
    
    session["user_id"] = user.idUsuario

    return jsonify({
        "id": user.idUsuario,
        "nome": user.nome
    })

## Rota de logout
@app.route("/logout", methods=["POST"])
def logout_user():
    session = Session()
    session.pop("user_id")
    return "200"