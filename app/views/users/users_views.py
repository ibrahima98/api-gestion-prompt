from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users.auth_users import create_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/create_user', methods=['POST'])
@jwt_required()
def create_new_user():
    current_user = get_jwt_identity()
    if not current_user.get('admin'):
        return jsonify({"msg": "Admins only!"}), 403

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    adresse = data.get('adresse')
    numero_tel = data.get('numero_tel')
    password = data.get('password')
    id_groupe = data.get('id_groupe')

    if not username or not email or not adresse or not numero_tel or not password or not id_groupe:
        return jsonify({"msg": "Missing required fields"}), 400

    hashed_password = generate_password_hash(password)
    create_user(username, email, adresse, numero_tel, hashed_password, current_user['id'], id_groupe)

    return jsonify({"msg": "User created successfully"}), 201
