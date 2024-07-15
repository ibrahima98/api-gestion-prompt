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

    if not username or not email or not adresse or not password :
        return jsonify({"msg": "Vous avez oublié un champ"}), 400

    mdp_hache = generate_password_hash(password)
    create_user(username, email, adresse, numero_tel, mdp_hache, user_actuel['id'], id_groupe)

    return jsonify({"msg": "Utilisateur créé avec succès"}), 201

@user_bp.route('/modifier_prompt', methods=['POST'])
@jwt_required()
def modifier_prompt():
    user_actuel = get_jwt_identity()
    data = request.get_json()
    id_demande = data.get('id_demande')

    if not id_demande:
        return jsonify({"msg": "ID de la demande requis"}), 400

    db = get_db()
    cursor = db.cursor()

    # Fetch the modification request
    cursor.execute(
        """
        SELECT id_prompt, nouvelle_description, nouvelle_titre, status 
        FROM demande_modification_prompt
        WHERE id_demande = %s
        """,
        (id_demande,)
    )
    demande = cursor.fetchone()

    if not demande:
        return jsonify({"msg": "Demande de modification non trouvée"}), 404

    id_prompt, nouvelle_description, nouvelle_titre, status_demande = demande

    cursor.execute(
        """
        SELECT id_users FROM prompts WHERE id_prompt = %s
        """,
        (id_prompt,)
    )
    prompt = cursor.fetchone()

    if prompt[0] != user_actuel['id']:
        return jsonify({"msg": "Vous n'êtes pas autorisé à modifier ce prompt"}), 403

    cursor.execute(
        """
        UPDATE prompts SET description = %s, titre = %s, date_modification = NOW()
        WHERE id_prompt = %s
        """,
        (nouvelle_description, nouvelle_titre, id_prompt)
    )

    cursor.execute(
        """
        UPDATE demande_modification_prompt SET status = 'approuvée' WHERE id_demande = %s
        """,
        (id_demande,)
    )

    db.commit()
    cursor.close()

    return jsonify({"msg": "Prompt modifié avec succès"}), 200
