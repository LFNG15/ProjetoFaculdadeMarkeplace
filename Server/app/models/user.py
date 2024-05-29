from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/Marketplace'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class User(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(12), nullable=False)
    nome_usuario = db.Column(db.String(15), unique=True, nullable=False)
    nome_pessoa = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(14))
    cep = db.Column(db.String(8))
    endereco = db.Column(db.String(255))
    complemento = db.Column(db.String(255))
    has_ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_cadastro = db.Column(db.TIMESTAMP, nullable=False, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'email': self.email,
            'senha': self.senha,
            'nome_usuario': self.nome_usuario,
            'nome_pessoa': self.nome_pessoa,
            'cpf': self.cpf,
            'endereco': self.endereco,
            'complemento': self.endereco,
            'has_ativo': self.has_ativo,
            'data_cadastro': self.data_cadastro
        }