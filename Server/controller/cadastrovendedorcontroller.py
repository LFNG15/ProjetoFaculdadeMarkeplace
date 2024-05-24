from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

app = Flask(__name__)

Vendedor = []

@app.route('/Vendedor', methods=['POST'])
@jwt_required()  
def create_Vendedor():
    current_user_id = get_jwt_identity() 
    new_vendedor_data = request.json
    new_vendedor = Vendedor(
        name=new_vendedor_data['name'],
        id=current_user_id,
        cnpj=new_vendedor_data['cnpj']
    )
    vendedor.append(new_vendedor.to_dict())
    return jsonify(new_vendedor.to_dict()), 201

@app.route('/Vendedor', methods=['GET'])
def get_Vendedors():
    return jsonify(Vendedor)

@app.route('/Vendedor/<int:Vendedor_id>', methods=['GET'])
def get_Vendedor(vendedor_id):
    Vendedor = next((vendedor for vendedor in vendedor if vendedor['id'] == vendedor_id), None)
    if Vendedor:
        return jsonify(Vendedor)
    return jsonify({'message': 'Vendedor não encontrado'}), 404

@app.route('/Vendedor/<int:Vendedor_id>', methods=['PUT'])
def update_Vendedor(vendedor_id):
    update_vendedor = request.json
    for i, Vendedor in enumerate(Vendedor):
        if Vendedor['id'] == vendedor_id:
            Vendedor[i] = update_vendedor
            return jsonify(update_vendedor)
    return jsonify({'message': 'Vendedor não encontrado'}), 404

@app.route('/Vendedors/<int:Vendedor_id>', methods=['DELETE'])
def delete_Vendedor(vendedor_id):
    global vendedor
    Vendedor = [vendedor for vendedor in vendedor if vendedor['id'] != vendedor_id]
    return jsonify({'message': 'Vendedor excluído com sucesso'}), 200
