 🏨 Projet Hôtel

Ce projet est une application de gestion hôtelière qui combine un **frontend Angular** et un **backend API** (FastAPI).  
L’objectif est de faciliter la gestion des réservations, des clients et des services hôteliers grâce à une architecture moderne.

---

## 📂 Structure du projet

projet-hotel/
│
├── PRJ/
│ ├── intelligent-hotel-ui/ # Frontend (Angular)
│ ├── intelligent-hotel-api/ # Backend (FastAPI ou autre API)
│
├── docs/ # Documentation du projet
└── README.md # Documentation principale

yaml
Copier le code

---

## ⚙️ Installation

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/zack-morpho/projet-hotel
cd projet-hotel
2️⃣ Backend (API)
Aller dans le dossier de l’API :

bash
Copier le code
cd PRJ/intelligent-hotel-api
Créer un environnement virtuel (optionnel mais recommandé) :

bash
Copier le code
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Installer les dépendances :

bash
Copier le code
pip install -r requirements.txt
Lancer le serveur :

bash
Copier le code
uvicorn main:app --reload
👉 L’API sera disponible sur : http://127.0.0.1:8000

3️⃣ Frontend (Angular)
Aller dans le dossier Angular :

bash
Copier le code
cd PRJ/intelligent-hotel-ui
Installer les dépendances :

bash
Copier le code
npm install
Lancer le projet :

bash
Copier le code
ng serve
👉 Le frontend sera accessible sur : http://localhost:4200
