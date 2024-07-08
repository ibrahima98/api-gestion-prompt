from app.db import get_db

def create_user(username, email, adresse, numero_tel, hashed_password, id_admin, id_groupe):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO users (username, email_users, adresse_users, numero_tel_users, mdp_users, id_admin, id_groupe_users)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (username, email, adresse, numero_tel, hashed_password, id_admin, id_groupe)
    )
    db.commit()
    cursor.close()
