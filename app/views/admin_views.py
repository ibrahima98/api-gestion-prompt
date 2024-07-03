from flask import Blueprint, jsonify
from app.db import get_db

bp = Blueprint('admin', __name__)

@bp.route('/users_admin')
def get_users_admin():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM admin')
    users_admin = cursor.fetchall()
    cursor.close()

    return jsonify(users_admin)
