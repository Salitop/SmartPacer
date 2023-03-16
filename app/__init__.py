from ast import If
from pickle import GET
from urllib import response
from flask import Flask, render_template, request,redirect, url_for
from mvc_flask import FlaskMVC
import sys  
from .models import Session,engine,Noticias
import sqlalchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
FlaskMVC(app)

@app.route("/")
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()

@app.route("/calculo")
def calcular():
    qtdnotasP = select count(notasSprintP) where etapa = 1 
    totalp = Sum(notasSprintP) / qtdnotasp

        qtdnotasA = select count(notasSprintA) where etapa = 1 
    totalA = Sum(notasSprintA) / qtdnotasA

        qtdnotasC = select count(notasSprintC) where etapa = 1 
    totalC = Sum(notasSprintC) / qtdnotasC

        qtdnotasER = select count(notasSprintER) where etapa = 1 
    totalER = Sum(notasSprintER) / qtdnotasER
    
    return render_template('tela_exibicao')