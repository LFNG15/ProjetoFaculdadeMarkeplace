from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.model import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/auth/login', methods=['POST'])
def Login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({'messages': 'Dados inválidos'}), 401