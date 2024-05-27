from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from __init__ import db

vendedor_bp = Blueprint('vendedor_bp',__name__)

Vendedor = []

@vendedor_bp.route('/Vendedor', methods=['POST'])
@jwt_required()  
def create_Vendedor():
    current_user_id = get_jwt_identity() 
    new_vendedor_data = request.json
    new_vendedor = Vendedor(
        name=new_vendedor_data['nome'],
        id=current_user_id,
        cnpj=new_vendedor_data['cnpj']
    )
    ##vendedor.append(new_vendedor.to_dict())
    db.session.add(new_vendedor)
    db.session.commit()
    return jsonify(new_vendedor.to_dict()), 201

@vendedor_bp.route('/Vendedor', methods=['GET'])
def get_Vendedors():
    vendedores = Vendedor.query.all()
    return jsonify([vendedor.to_dict() for vendedor in vendedores])

@vendedor_bp.route('/Vendedor/<int:Vendedor_id>', methods=['GET'])
def get_Vendedor(vendedor_id):
    ##Vendedor = next((vendedor for vendedor in vendedor if vendedor['id'] == vendedor_id), None)
    vendedor = Vendedor.query.get(vendedor_id)
    if Vendedor:
        return jsonify(vendedor.to_dict())
    return jsonify({'message': 'Vendedor não encontrado'}), 404

@vendedor_bp.route('/Vendedor/<int:Vendedor_id>', methods=['PUT'])
def update_Vendedor(vendedor_id):
    update_vendedor_data = request.json
    vendedor = Vendedor.query.get(vendedor_id)
    if vendedor:
        vendedor.nome = update_vendedor_data.get('nome', vendedor.nome)
        vendedor.cnpj = update_vendedor_data.get('cnpj', vendedor.cnpj)
        db.session.commit()
    return jsonify({'message': 'Vendedor não encontrado'}), 404

@vendedor_bp.route('/Vendedors/<int:Vendedor_id>', methods=['DELETE'])
def delete_Vendedor(vendedor_id):
    ##global vendedor
    ##Vendedor = [vendedor for vendedor in vendedor if vendedor['id'] != vendedor_id]
    vendedor = Vendedor.query.get(vendedor_id)
    if vendedor:
        db.session.delete(vendedor)
        db.session.commit()
        return jsonify({'message': 'Vendedor excluído com sucesso'}),200
    return jsonify({'message': 'Vendedor não encontrado'}), 404
