from urllib import response
from flask import Flask, render_template, request,redirect, url_for, jsonify
from .models import Session,engine, UsuarioPacer, Sprint

app = Flask(__name__)

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

@app.route("/obterTodasSprints",methods = ['GET'])
def obterTodasSprints():
    session = Session()
    sprints =  session.query(Sprint).filter_by(Ativo = 1).all()
    
    todas_sprints = [{'idsprint':sprint.IdSprint,'ano':sprint.Ano,'semestre':sprint.Semestre,'descricao':sprint.Descricao} for sprint in sprints]
         
    return jsonify(todas_sprints)

    #  IdSprint = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    # Ano = sqlalchemy.Column(sqlalchemy.SmallInteger, nullable=False)
    # Semestre = sqlalchemy.Column(sqlalchemy.SmallInteger, nullable=False)
    # Descricao = sqlalchemy.Column(sqlalchemy.String(20))
    # Ativo = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)