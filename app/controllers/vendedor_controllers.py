from flask import Flask, request, jsonify, abort
from model.vendedor import Vendedor, db

app = Flask(__name__)

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