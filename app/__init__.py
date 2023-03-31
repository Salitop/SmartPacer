from urllib import response
from flask import Flask, render_template, request,redirect, url_for, jsonify
from flask_cors import CORS
from .models import *
from sqlalchemy import create_engine, Column, Integer, String, func

app = Flask(__name__)
CORS(app)

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
    # filtro = session.query(UsuarioPacer,UsuarioEquipe,Usuario)\
    # .join(Usuario, UsuarioPacer.IdUsuarioAvaliado == Usuario.IdUsuario)\
    # .join(UsuarioEquipe, Usuario.IdUsuario == UsuarioEquipe.UsuarioId)\
    # .filter(UsuarioPacer.IdSprint == request.args.get('idsprint'),\
    #  UsuarioEquipe.EquipeId ==request.args.get('idequipe'))\
    # .distinct().all()

    filtro = session.query(UsuarioPacer.IdUsuarioAvaliado,UsuarioEquipe,Usuario)\
    .join(Usuario, UsuarioPacer.IdUsuarioAvaliado == Usuario.IdUsuario)\
    .join(UsuarioEquipe, Usuario.IdUsuario == UsuarioEquipe.UsuarioId)\
    .filter(UsuarioPacer.IdSprint == request.args.get('idsprint'),\
     UsuarioEquipe.EquipeId ==request.args.get('idequipe'))\
    .distinct().all()


    #pegar todas as notas por aluno, dar um count
    # filtroEquipeSprint =  session.query(EquipeSprint).filter_by(IdEquipe = data['idequipe'], IdSprint = data['idsprint']).all()
    
    # return print(filtro)
    # todas_sprints = [{'nomealuno':aluno.Usuario.Nome} for aluno in filtro]
    for aluno in filtro:
        # notasAluno = session.query(UsuarioPacer).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).all()
        notasAlunoA = session.query(func.sum(UsuarioPacer.NotaA)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        qtdNotasA = session.query(func.count(UsuarioPacer.NotaA)).filter_by(IdUsuarioAvaliado = aluno.Usuario.IdUsuario).scalar()
        total = notasAlunoA/qtdNotasA
        print(total)
        # for notasA in notasAluno:
        #     print(notasA.NotaA)
    return jsonify('ok')