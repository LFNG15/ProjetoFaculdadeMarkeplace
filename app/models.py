from app import db
from sqlalchemy.sql import func

class Usuario(db.Model):
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
    has_ativo = db.Column(db.Boolean, default=True)
    data_cadastro = db.Column(db.DateTime, default=func.now())

class Vendedor(db.Model):
    id_vendedor = db.Column(db.Integer, primary_key=True)
    cpnj = db.Column(db.String(14), unique=True, nullable=False)
    fk_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    has_ativo = db.Column(db.Boolean, default=True)
    data_cadastro = db.Column(db.DateTime, default=func.now())
    
    usuario = db.relationship('Usuario', backref=db.backref('vendedores', lazy=True))

class Pedido(db.Model):
    id_pedido = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    fk_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    fk_id_produto = db.Column(db.Integer, db.ForeignKey('produto.id_produto'), nullable=False)
    data_criacao = db.Column(db.DateTime, default=func.now())
    has_ativo = db.Column(db.Boolean, default=True)

class Pagamento(db.Model):
    id_pagamento = db.Column(db.Integer, primary_key=True)
    has_pagamento = db.Column(db.Boolean, default=False, nullable=False)
    fk_id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
    has_ativo = db.Column(db.Boolean, default=True)
    data_pagamento = db.Column(db.DateTime, onupdate=func.now())