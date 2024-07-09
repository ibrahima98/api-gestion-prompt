from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.prompt.prompt import *

prompt_bp = Blueprint('prompt', __name__)

@prompt_bp.route('/create_prompt', methods=['POST'])
@jwt_required()
def create_new_prompt():
    user_actuel = get_jwt_identity()
    data = request.get_json()
    titre = data.get('titre')
    description = data.get('description')

    if not titre or not description:
        return jsonify({"msg": "Le Titre et la description sont requis"}), 400

    prompt_id = create_prompt(titre, description, user_actuel['id'])
    return jsonify({"msg": "le prompt à été creer avec succes "}), 201


@prompt_bp.route('/<int:prompt_id>', methods=['GET'])
def get_prompt_info(prompt_id):
    prompt = get_prompt(prompt_id)
    if not prompt:
        return jsonify({"msg": "pas de prompt disponible"}), 404

    return jsonify({
        "id_prompt": prompt[0],
        "titre": prompt[1],
        "description": prompt[2],
        "status": prompt[3],
        "prix": prompt[4],
        "id_users": prompt[5],
        "date_creation_prompt": prompt[6],
        "date_modification": prompt[7]
    }), 200

@prompt_bp.route('/en_attente', methods=['GET'])
@jwt_required()
def get_prompts_en_attente():
    prompts = get_prompts_status_en_attente()
    if not prompts:
        return jsonify({"msg": "pas de prompts disponibles"}), 404

    prompts_list = []
    for prompt in prompts:
        prompts_list.append({
            "id_prompt": prompt[0],
            "titre": prompt[1],
            "description": prompt[2],
            "status": prompt[3],
            "prix": prompt[4],
            "id_users": prompt[5],
            "date_creation_prompt": prompt[6],
            "date_modification": prompt[7]
        })

    return jsonify(prompts_list), 200