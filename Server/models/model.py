from app import db

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