from app.db import get_db

def create_prompt(titre, description, user_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO prompts (titre, description, status, prix, id_users, date_creation_prompt, date_modification)
        VALUES (%s, %s, 'en attente', 1000, %s, NOW(), NOW())
        RETURNING id_prompt
        """,
        (titre, description, user_id)
    )
    prompt_id = cursor.fetchone()[0]
    db.commit()
    cursor.close()
    return prompt_id

def get_prompt(prompt_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id_prompt, titre, description, status, prix, id_users, date_creation_prompt, date_modification 
        FROM prompts 
        WHERE id_prompt = %s
        """,
        (prompt_id,)
    )
    prompt = cursor.fetchone()
    cursor.close()
    return prompt

def get_prompts_with_status_en_attente():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id_prompt, titre, description, status, prix, id_users, date_creation_prompt, date_modification 
        FROM prompts 
        WHERE status = 'en attente'
        """
    )
    prompts = cursor.fetchall()
    cursor.close()
    return prompts

def get_prompts_actifs():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        """
        SELECT id_prompt, titre, description, status, prix, id_users, date_creation_prompt, date_modification 
        FROM prompts 
        WHERE status = 'active'
        """
    )
    prompts = cursor.fetchall()
    cursor.close()
    return prompts

def acheter_prompt(prompt_id, session_id):
    db = get_db()
    cursor = db.cursor()
    try:
        # Vérifiez d'abord si le prompt est disponible et actif
        cursor.execute("SELECT id_prompt FROM prompts WHERE id_prompt = %s AND status = 'active'", (prompt_id,))
        prompt = cursor.fetchone()
        if prompt:
            print(f"Prompt trouvé : {prompt}")
            print(f"Session ID : {session_id}")
            # Insérez une nouvelle vente dans la table "vente"
            cursor.execute(
                """
                INSERT INTO vente (id_session_invite, id_prompt)
                VALUES (%s, %s)
                """,
                (session_id, prompt_id)
            )
            db.commit()
            return True
        else:
            print("Prompt non trouvé ou non actif")
            return False
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cursor.close()