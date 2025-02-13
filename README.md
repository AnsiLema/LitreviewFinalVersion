# LITRevu 📚🔍

LITRevu est une application web développée en Django permettant aux utilisateurs de publier des demandes de critiques sur des œuvres littéraires et de rédiger des critiques en réponse à ces demandes. Elle intègre un système de suivi d'utilisateurs ainsi que la possibilité de bloquer certains profils pour contrôler la visibilité des publications.

---

## 🚀 Fonctionnalités principales

- **Gestion des utilisateurs** : Inscription, connexion et gestion des abonnements.
- **Création et modification de tickets** : Publiez des demandes de critiques sur des œuvres.
- **Critiques associées aux tickets** : Répondez aux demandes de critiques avec une évaluation et un avis détaillé.
- **Flux personnalisé** : Affichage des publications des utilisateurs suivis et des critiques en réponse à ses propres tickets.
- **Blocage des utilisateurs** : Empêchez certains utilisateurs de voir votre contenu.
- **Pagination** : Navigation fluide à travers les publications.
- **Accessibilié** : Interface qui respecte les bonnes pratiques d'accessibilité du reférenciel WCAG

---

## 🏗️ Installation et utilisation

### 1️⃣ Prérequis

- Python 3.12+

### 2️⃣ Installation

1. Clonez le projet :
   ```bash
   git clone https://github.com/AnsiLema/LitreviewFinalVersion.git
   
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv .venv
   
   source .venv/bin/activate  # Sur macOS/Linux
   
   .venv/Scripts/activate     # Sur Windows
   ```

3. Installez les dépendances Python :
   ```bash
   cd LitReviewFinalVersion
   
   pip install -r requirements.txt
   ```

4. Appliquez les migrations de la base de données :
   ```bash
   python manage.py migrate
   ```

5. Démarrez le serveur Django :
   ```bash
   python manage.py runserver
   ```

6. Accédez à l'application via :
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Structure du projet

```plaintext
LitReviewFinalVersion/
├── .venv/                        # Environnement virtuel Python
├── authentication/               # Gestion des utilisateurs (connexion, inscription, suivi)
│   ├── templates/authentication/ # Templates pour l'authentification
│   │   ├── follow_user_form.html
│   │   ├── login.html
│   │   └── signup.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── images/                       # Répertoire pour stocker des images
├── litreview/                    # Configuration principale du projet Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Configuration globale du projet
│   ├── urls.py                   # Routage URL principal
│   └── wsgi.py
├── reviews/                      # Gestion des critiques et logique de l'application principale
│   ├── migrations/
│   ├── templates/reviews/        # Templates spécifiques aux critiques
│   │   ├── partials/
│   │   │   └── home.html
│   ├── templatetags/             # Tags personnalisés pour les templates
│   │   ├── __init__.py
│   │   └── reviews_extras.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── static/                       # Fichiers statiques (CSS, JavaScript, images)
├── templates/                    # Templates de base partagés
│   └── base.html
├── tickets/                      # Gestion des demandes de critiques (tickets)
│   ├── migrations/
│   ├── templates/tickets/        # Templates spécifiques aux tickets
│   │   ├── posts.html
│   │   ├── review_confirm_delete.html
│   │   ├── review_create.html
│   │   ├── review_detail.html
│   │   ├── review_list.html
│   │   ├── review_update.html
│   │   ├── ticket_and_review_upload.html
│   │   ├── ticket_confirm_delete.html
│   │   ├── ticket_create.html
│   │   ├── ticket_detail.html
│   │   └── ticket_update.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── .flake8                       # Configuration pour linting
├── db.sqlite3                    # Base de données SQLite
├── manage.py                     # Script principal pour exécuter le projet
├── README.md                     # Fichier de documentation
└── requirements.txt              # Dépendances du projet
```

---

## 💡 Fonctionnement

- **Tickets (demandes de critiques)** :  
  Les utilisateurs peuvent créer des tickets avec des informations sur une œuvre (titre, description), à laquelle d'autres utilisateurs peuvent répondre avec des critiques.

- **Critiques** :  
  Les critiques incluent un avis sur l'œuvre ciblée par un ticket.

- **Suivi et blocage d'utilisateurs** :  
  Chaque utilisateur peut librement suivre ou bloquer d'autres profils pour personnaliser son flux d'affichage.

- **Pagination** :  
  L'expérience utilisateur est simplifiée grâce à une pagination qui facilite la navigation dans les publications.

---

## 🧩 Technologies utilisées

- **Django Framework** : Backend robuste et architecture web.
- **HTML5 / CSS3** : Templates front-end simples et adaptables.
- **SQLite** : Base de données intégrée (par défaut).
- **Bootstrap** : Mise en page responsive.

---

## 📧 Contact

Réalisé par A'nsi. N'hésitez pas à me contacter par email :  
**ansilema@gmail.com**