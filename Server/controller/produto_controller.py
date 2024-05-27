from flask import Blueprint, jsonify, request

produto_bp = Blueprint('produto_pb',__name__)
Produto = []

@produto_bp.route('/Produto', methods=['POST'])
def create_Produto():
    Produto_data = request.json
    new_Produto = Produto(
        name=Produto_data['name'],
        price=Produto_data['price'],
        promo_price=Produto_data['promo_price'],
        quantity=Produto_data['quantity'],
        description=Produto_data['description'],
        images=Produto_data['images'],
        variations=Produto_data['variations']
    )
    Produto.append(new_Produto.to_dict())
    return jsonify(new_Produto.to_dict()), 201

@produto_bp.route('/Produto/<int:Produto_id>', methods=['PUT'])
def update_Produto(Produto_id):
    Produto_data = request.json
    for Produto in Produto:
        if Produto['id'] == Produto_id:
            Produto.update(Produto_data)
            return jsonify(Produto)
    return jsonify({'message': 'Produto não encontrado'}), 404

@produto_bp.route('/Produto/<int:Produto_id>', methods=['DELETE'])
def delete_Produto(Produto_id):
    global Produto
    Produto = [Produto for Produto in Produto if Produto['id'] != Produto_id]
    return jsonify({'message': 'Produto excluído com sucesso'}), 200