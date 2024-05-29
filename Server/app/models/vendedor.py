from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/Marketplace'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Vendedor(db.Model):
    id_vendedor = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    fk_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    has_ativo = db.Column(db.Boolean, nullable=False, default=True)
    data_cadastro = db.Column(db.TIMESTAMP, nullable=False, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id_vendedor': self.id_vendedor,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'fk_id_usuario': self.fk_id_usuario,
            'has_ativo': self.has_ativo,
            'data_cadastro': self.data_cadastro
        }
    