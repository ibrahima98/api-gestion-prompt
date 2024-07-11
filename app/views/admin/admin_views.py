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
