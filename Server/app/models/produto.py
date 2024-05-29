from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/Marketplace'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    estoque = db.Column(db.Integer)
    fk_id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'), nullable=False)
    fk_id_vendedor = db.Column(db.Integer, db.ForeignKey('vendedor.id_vendedor'), nullable=False)
    has_ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_criacao = db.Column(db.TIMESTAMP, nullable=False, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id_produto': self.id_produto,
            'nome': self.nome,
            'preco': self.preco,
            'estoque': self.estoque,
            'fk_id_categoria': self.fk_id_categoria,
            'fk_id_vendedor': self.fk_id_vendedor,
            'has_ativo': self.has_ativo,
            'data_criacao': self.data_criacao
        }