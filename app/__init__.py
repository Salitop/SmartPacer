from urllib import response
from flask import Flask, render_template, request,redirect, url_for, jsonify
# from mvc_flask import FlaskMVC
# import sys  
from .models import Session,engine,Noticias
# import sqlalchemy
# from datetime import datetime
# from sqlalchemy.ext.declarative import declarative_base

# app = Flask(__name__)
# FlaskMVC(app)

@app.route("/")
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route("/cadastrarNotas",methods = ['POST'])
def calcular():
    app.run()

    # if request.method == "GET":
    #     return render_template('cadastrar.html')
    # else:
    novoPacer = session.query(usuariopacer)
    data = request.get_json()
    novoPacer.notaP = data['p']
    novoPacer.notaA = data['a']
    novoPacer.notaC = data['c']
    novoPacer.notaER = data['er']
    novoPacer.usuario = data['usuario']
    novoPacer.usuarioAvaliado = data['usuarioAvaliado']
    novoPacer.idSprint = data['idSprint']
   
    session.add(novoPacer)
    session.commit()
         
        #  return render_template('visualizar.html',noticia=noticia)
    return jsonify({'result':'deu certo', 'p': notaP,'a': notaA,'c': notaC,'er': notaER})

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