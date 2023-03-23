from urllib import response
from flask import Flask, render_template, request,redirect, url_for, jsonify
from flask_bcrypt import Bcrypt ## modulo para encriptar as senhas dos usuarios

from .models import Session,engine, UsuarioPacer


app = Flask(__name__)

bcrypt = Bcrypt(app)

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


## rota para login
@app.route("/login", methods=["GET", "POST"])
def login():
    app.run()
    
    data = request.get_json()
    ## obtem nome e senha inseridos no formulario
    ## faz a busca na yabela Usuario pelo nome
    ## compara a senha inserida com a senha no banco
    usuarioNome = data['nome']
    usuarioSenha = data['senha']
    usuario = Usuario.query.filter_by(nome=usuarioNome).first()
    if usuario:
        if usuario.senha == usuarioSenha:
            return "Login bem sucedido"


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