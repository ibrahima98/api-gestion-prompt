from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db import get_db

bp = Blueprint('admin', __name__)

@bp.route('/admin/data', methods=['GET']) 
@jwt_required()
def admin_data():
    current_user = get_jwt_identity()
    if not current_user['admin']:
        return jsonify({"msg": "Admins only!"}), 403

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    return jsonify(users), 200

@bp.route('/demande_modification_prompt', methods=['POST'])
@jwt_required()
def demande_modification_prompt():
    user_actuel = get_jwt_identity()
    if not user_actuel.get('admin'):
        return jsonify({"msg": "Vous n'êtes pas un administrateur!"}), 403

    data = request.get_json()
    id_prompt = data.get('id_prompt')
    nouvelle_description = data.get('nouvelle_description')
    nouvelle_titre = data.get('nouvelle_titre')

    if not id_prompt or not nouvelle_description or not nouvelle_titre:
        return jsonify({"msg": "Tous les champs sont requis"}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO demande_modification_prompt (id_prompt, nouvelle_description, nouvelle_titre)
        VALUES (%s, %s, %s)
        RETURNING id_demande
        """,
        (id_prompt, nouvelle_description, nouvelle_titre)
    )
    id_demande = cursor.fetchone()[0]
    db.commit()
    cursor.close()

    return jsonify({"msg": "Demande de modification créée avec succès", "id_demande": id_demande}), 201