from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)

sellers = []

@app.route('/sellers', methods=['POST'])
@jwt_required()  
def create_seller():
    current_user_id = get_jwt_identity() 
    new_seller_data = request.json
    new_seller = Seller(
        name=new_seller_data['name'],
        id=current_user_id,
        cnpj=new_seller_data['cnpj']
    )
    sellers.append(new_seller.to_dict())
    return jsonify(new_seller.to_dict()), 201

@app.route('/sellers', methods=['GET'])
def get_sellers():
    return jsonify(sellers)

@app.route('/sellers/<int:seller_id>', methods=['GET'])
def get_seller(seller_id):
    seller = next((seller for seller in sellers if seller['id'] == seller_id), None)
    if seller:
        return jsonify(seller)
    return jsonify({'message': 'Vendedor não encontrado'}), 404

@app.route('/sellers/<int:seller_id>', methods=['PUT'])
def update_seller(seller_id):
    update_seller = request.json
    for i, seller in enumerate(sellers):
        if seller['id'] == seller_id:
            sellers[i] = update_seller
            return jsonify(update_seller)
    return jsonify({'message': 'Vendedor não encontrado'}), 404

@app.route('/sellers/<int:seller_id>', methods=['DELETE'])
def delete_seller(seller_id):
    global sellers
    sellers = [seller for seller in sellers if seller['id'] != seller_id]
    return jsonify({'message': 'Vendedor excluído com sucesso'}), 200
