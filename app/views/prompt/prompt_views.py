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
    return jsonify({"msg": "le prompt a ete creer avec succes "}), 201


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
    prompts = get_prompts_with_status_en_attente()
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

@prompt_bp.route('/', methods=['GET'])
def get_prompts_actifs_default():
    prompts_actifs = get_prompts_actifs()
    prompts_list = []

    for prompt in prompts_actifs:
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

    return jsonify(prompts_list)

@prompt_bp.route('/<int:prompt_id>/buy', methods=['POST'])
def buy_prompt(prompt_id):
    data = request.get_json()
    
    # Ajoutez des logs pour vérifier ce que le serveur reçoit
    print("Data received:", data)

    if not data:
        return jsonify({"msg": "Corps de la requête JSON non reçu ou mal formé"}), 400

    session_id = data.get('session_id')

    if not session_id:
        return jsonify({"msg": "Session ID est requis"}), 400

    try:
        purchase_result = acheter_prompt(prompt_id, session_id)
        if purchase_result:
            return jsonify({"msg": "Prompt acheté avec succès"}), 200
        else:
            return jsonify({"msg": "Impossible d'acheter le prompt"}), 400
    except Exception as e:
        return jsonify({"msg": str(e)}), 500