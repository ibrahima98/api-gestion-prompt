# 🚗 Auto-École Connect - Plateforme d'Annonces pour Auto-Écoles

## 📋 Description Globale
Auto-École Connect est une plateforme web permettant aux auto-écoles de publier leurs annonces et aux futurs élèves de trouver l'auto-école idéale. Les auto-écoles peuvent publier leurs offres, promotions et localisation, tandis que les élèves peuvent rechercher, comparer et laisser des avis.

## 🏗 Architecture du Projet
├── backend/
│ ├── app/
│ │ ├── models/
│ │ │ ├── autoecole.py
│ │ │ ├── avis.py
│ │ │ ├── user.py

│ │ │ └── annonce.py
│ │ ├── routes/
│ │ └── extensions/
│ ├── migrations/
│ └── requirements.txt
└── frontend/
├── public/
├── src/
│ ├── components/
│ ├── pages/
│ └── services/
└── package.json

## 🚀 Installation Rapide
1. Cloner le projet
    git clone lien repos

2. Backend Setup
    cd backend
    python -m venv venv
    source venv/Scripts/activate # Windows
    pip install -r requirements.txt
Créer le fichier .env
    echo "FLASK_APP=wsgi.py
    FLASK_ENV=development
    DATABASE_URL=postgresql://postgres:Passer01@localhost/autoecole_db" > .env

# Initialiser la base de données
    flask db upgrade
    flask run
3. Frontend Setup (dans un nouveau terminal)
    cd ../frontend
    npm install
    npm start
    
## 🔑 Fonctionnalités Principales

### 👨‍🏫 Pour les Auto-Écoles
- Publication d'annonces et promotions
- Gestion du profil et des informations
- Tableau de bord des statistiques
- Gestion des disponibilités
- Publication des tarifs et forfaits

### 👨‍🎓 Pour les Élèves
- Recherche avancée d'auto-écoles
- Filtrage par localisation, prix, et options
- Système de notation et avis
- Comparaison des forfaits
- Inscription aux notifications

## 🛠 Stack Technique

### Backend
- Python 3.11
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-JWT-Extended
- Flask-CORS

### Frontend
- React.js
- Material-UI
- Redux Toolkit
- Axios
- Leaflet (pour les cartes)

## 📡 API Endpoints

### Auto-Écoles

Liste et recherche
GET /api/autoecoles
GET /api/autoecoles/search?ville=Paris&prix_max=1500
Gestion des profils
POST /api/autoecoles
PUT /api/autoecoles/{id}
Annonces et promotions
POST /api/autoecoles/{id}/annonces

### Avis et Notes
POST /api/autoecoles/{id}/avis
GET /api/autoecoles/{id}/avis

## 📱 Pages Principales (Frontend)

1. **Page d'Accueil**
   - Barre de recherche
   - Carte interactive
   - Promotions en vedette

2. **Recherche d'Auto-École**
   - Filtres avancés
   - Vue liste/carte
   - Comparateur

3. **Profil Auto-École**
   - Informations détaillées
   - Galerie photos
   - Avis et notes
   - Forfaits disponibles

4. **Espace Auto-École**
   - Tableau de bord
   - Gestion des annonces
   - Statistiques

## 🔄 Commandes Utiles

```bash
# Backend
flask run  # Lancer le serveur
flask db upgrade  # Mettre à jour la base de données
flask db migrate -m "message"  # Créer une migration

# Frontend
npm start  # Lancer l'application React
npm run build  # Build de production
npm test  # Lancer les tests
```

## 📦 Base de Données

```bash
# Export
pg_dump -U postgres -h localhost autoecole_db > backup.sql

# Import
psql -U postgres -h localhost autoecole_db < backup.sql
```

## 🌐 Variables d'Environnement

### Backend (.env)
```env
FLASK_APP=wsgi.py
FLASK_ENV=development
DATABASE_URL=postgresql://postgres:123456@localhost/autoecole_db
JWT_SECRET_KEY=votre-secret-key
```

### Frontend (.env)


## 🔒 Sécurité
- JWT pour l'authentification
- CORS configuré
- Validation des données
- Protection contre les injections SQL
- Hashage des mots de passe


## 🚀 Déploiement

1. **Préparer le Backend**

3. **Configuration Nginx**


## 📝 TODO
- [ ] Système de notifications
- [ ] Chat en direct
- [ ] Paiement en ligne
- [ ] Application mobile
- [ ] Système de réservation

## 👥 Contribution
1. Fork le projet
2. Créez votre branche (`git checkout -b feature/NouvelleFonctionnalite`)
3. Commit (`git commit -m 'Ajout nouvelle fonctionnalité'`)
4. Push (`git push origin feature/NouvelleFonctionnalite`)
5. Créez une Pull Request

## 📄 Licence
Ce projet est sous licence MIT.
```
