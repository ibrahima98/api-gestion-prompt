from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from app.models.users.auth_users import create_user
from app.db import get_db

user_bp = Blueprint('user', __name__)

@user_bp.route('/create_user', methods=['POST'])
@jwt_required()
def create_new_user():
    user_actuel = get_jwt_identity()
    if not user_actuel.get('admin'):
        return jsonify({"msg": "Vous n'êtes pas un administrateur!"}), 403

    donnees = request.get_json()
    username = donnees.get('username')
    email = donnees.get('email')
    adresse = donnees.get('adresse')
    numero_tel = donnees.get('numero_tel')
    password = donnees.get('password')
    id_groupe = donnees.get('id_groupe')

    if not username or not email or not adresse or not numero_tel or not password or not id_groupe:
        return jsonify({"msg": "Vous avez oublié un champs"}), 400

    mdp_hache = generate_password_hash(password)
    create_user(username, email, adresse, numero_tel, mdp_hache, user_actuel['id'], id_groupe)

    return jsonify({"msg": "Utilisateur créer avec Succès"}), 201


@user_bp.route('/login_user', methods=['POST'])
def login_user():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({"msg": "Veuillez entrer un utilisateur et mot de passe "}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id_users, mdp_users FROM users WHERE email_users = %s", (email,))
    user = cursor.fetchone()

    if not user:
        return jsonify({"msg": "Mauvais email ou mot de passe"}), 401

    mdp_hache_restaure = user[1]

    if check_password_hash(mdp_hache_restaure, password):
        access_token = create_access_token(identity={'id': user[0], 'admin': False})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Mauvais email ou mot de passe"}), 401   