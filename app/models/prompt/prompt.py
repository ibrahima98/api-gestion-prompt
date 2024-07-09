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

def get_prompts_status_en_attente():
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