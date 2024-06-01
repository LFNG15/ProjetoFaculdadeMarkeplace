from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/Marketplace'


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
            'name': self.name,
            'cnpj': self.cnpj,
            'fk_id_usuario': self.fk_id_usuario,
            'has_ativo': self.has_ativo,
            'data_cadastro': self.data_cadastro
        }

# Create a new Vendedor
@app.route('/vendedores', methods=['POST'])
def create_vendedor():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'cnpj', 'fk_id_usuario')):
        abort(400)

    new_vendedor = Vendedor(
        name=data['name'],
        cnpj=data['cnpj'],
        fk_id_usuario=data['fk_id_usuario']
    )
    db.session.add(new_vendedor)
    db.session.commit()
    return jsonify(new_vendedor.to_dict()), 201

# Get all Vendedores
@app.route('/vendedores', methods=['GET'])
def get_vendedores():
    vendedores = Vendedor.query.all()
    return jsonify([vendedor.to_dict() for vendedor in vendedores])

# Get a specific Vendedor by id
@app.route('/vendedores/<int:id_vendedor>', methods=['GET'])
def get_vendedor(id_vendedor):
    vendedor = Vendedor.query.get_or_404(id_vendedor)
    return jsonify(vendedor.to_dict())

# Update a Vendedor
@app.route('/vendedores/<int:id_vendedor>', methods=['PUT'])
def update_vendedor(id_vendedor):
    vendedor = Vendedor.query.get_or_404(id_vendedor)
    data = request.get_json()
    if not data:
        abort(400)

    vendedor.name = data.get('name', vendedor.name)
    vendedor.cnpj = data.get('cnpj', vendedor.cnpj)
    vendedor.fk_id_usuario = data.get('fk_id_usuario', vendedor.fk_id_usuario)
    vendedor.has_ativo = data.get('has_ativo', vendedor.has_ativo)

    db.session.commit()
    return jsonify(vendedor.to_dict())

# Delete a Vendedor
@app.route('/vendedores/<int:id_vendedor>', methods=['DELETE'])
def delete_vendedor(id_vendedor):
    vendedor = Vendedor.query.get_or_404(id_vendedor)
    db.session.delete(vendedor)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)