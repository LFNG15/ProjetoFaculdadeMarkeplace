##CORRIGIR

from flask import Blueprint, jsonify, request
from app.models import Produto, db

produto_bp = Blueprint('produto_pb',__name__)
Produto = []

@produto_bp.route('/Produto', methods=['POST'])
def create_Produto():
    Produto_data = request.json
    new_Produto = Produto(
        nome=Produto_data['nome'],
        preco=Produto_data['preco'],
        estoque=Produto_data['estoque'],
        fk_id_categoria=Produto_data['fk_id_categoria'],
        fk_id_vendedor=Produto_data['fk_id_vendedor'],
        has_ativo=Produto_data.get('has_ativo', True)
    )
    db.session.add(new_Produto)
    db.session.commit()
    return jsonify(new_Produto.to_dict()), 201

@produto_bp.route('/Produto/<int:Produto_id>', methods=['PUT'])
def update_Produto(Produto_id):
    Produto_data = request.json
    produto = Produto.query.get(Produto_id)
    if produto is None:
        return jsonify({'message': 'Produto não encontrado'}), 404

    produto.nome = Produto_data.get('nome', produto.nome)
    produto.preco = Produto_data.get('preco', produto.preco)
    produto.estoque = Produto_data.get('estoque', produto.estoque)
    produto.fk_id_categoria = Produto_data.get('fk_id_categoria', produto.fk_id_categoria)
    produto.fk_id_vendedor = Produto_data.get('fk_id_vendedor', produto.fk_id_vendedor)
    produto.has_ativo = Produto_data.get('has_ativo', produto.has_ativo)

    db.session.commit()
    return jsonify(produto.to_dict())

@produto_bp.route('/Produto/<int:Produto_id>', methods=['DELETE'])
def delete_Produto(Produto_id):
    produto = Produto.query.get(Produto_id)
    if produto is None:
        return jsonify({'message': 'Produto não encontrado'}), 404

    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto excluído com sucesso'}), 200