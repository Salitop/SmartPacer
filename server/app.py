
from flask import Flask, request, abort, jsonify, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from models import db, User
from config import ApplicationConfig
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
bcrypt = Bcrypt(app)

server_session = Session(app)
db.init_app(app)
CORS(app, supports_credentials=True) 
with app.app_context():
    db.create_all()


@app.route("/@me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401
    
    user = User.query.filter_by(idUsuario=user_id).first()
    return jsonify({
        "id": user.idUsuario,
        "nome": user.nome
    }) 


@app.route("/register", methods=["POST"])
def register_user():
    nome = request.json["nome"]
    senha = request.json["senha"]
    login = request.json["login"]

    user_exists = User.query.filter_by(nome=nome).first() is not None
    if user_exists:
        return jsonify({"error": "Usuario já existe"})

    hashed_password = bcrypt.generate_password_hash(senha)
    new_user = User(nome=nome, senha=hashed_password, login=login)
    db.session.add(new_user)
    db.session.commit()

    session["user_id"] = new_user.idUsuario

    return jsonify({
        "id": new_user.idUsuario,
        "nome": new_user.nome
    })

@app.route("/login", methods=["POST"] )
def login_user():
    nome = request.json["nome"]
    senha = request.json["senha"]
    

    user = User.query.filter_by(nome=nome).first()
    if user is None:
        return jsonify({"error": "Não autorizado"}), 401
    
    if not bcrypt.check_password_hash(user.senha,senha):
        return jsonify({"error": "Não autorizado"}), 401
    
    
    session["user_id"] = user.idUsuario

    return jsonify({
        "id": user.idUsuario,
        "nome": user.nome
    })

@app.route("/logout", methods=["POST"])
def logout_user():
    session.pop("user_id")
    return "200"

if __name__ == "__main__":
    app.run(debug=True)