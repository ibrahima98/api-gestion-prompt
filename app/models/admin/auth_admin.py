from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/create_admin', methods=['POST'])
def create_admin():
    username = request.json.get('username_admin')
    email = request.json.get('email_admin')
    adresse = request.json.get('adresse_admin')
    numero_tel = request.json.get('numero_tel_admin')
    password = request.json.get('mdp')

    if not username or not email or not password:
        return jsonify({"msg": "Username, email et mot de passe est requis"}), 400

    mdp_hache = generate_password_hash(password)
    
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO admin (username_admin, email_admin, adresse_admin, numero_tel_admin, mdp) VALUES (%s, %s, %s, %s, %s)", 
                       (username, email, adresse, numero_tel, mdp_hache))
        db.commit()
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

    return jsonify({"msg": "Admin créer avec Succès"}), 201



@auth_bp.route('/login_admin', methods=['POST'])
def login_admin():
    email = request.json.get('email_admin')
    password = request.json.get('mdp')

    if not email or not password:
        return jsonify({"msg": "Email et mot de passe requis"}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id_admin, mdp FROM admin WHERE email_admin = %s", (email,))
    admin = cursor.fetchone()

    if not admin:
        return jsonify({"msg": "Mauvais email ou mot de passe "}), 401

    mdp_hache_restaure = admin[1]

    if check_password_hash(mdp_hache_restaure, password):
        access_token = create_access_token(identity={'id': admin[0], 'admin': True})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Mauvais email ou mot de passe "}), 401
