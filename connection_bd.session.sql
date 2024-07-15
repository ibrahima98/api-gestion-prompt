-- Supprimer la contrainte existante
ALTER TABLE vente DROP CONSTRAINT FK_PROMPT_VENTE;

-- Ajouter la nouvelle contrainte
ALTER TABLE vente ADD CONSTRAINT FK_PROMPT_VENTE
FOREIGN KEY (id_prompt)
REFERENCES prompts (id_prompt)
ON DELETE CASCADE
ON UPDATE CASCADE;
