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

---

## 🏗️ Installation et utilisation

### 1️⃣ Prérequis

- Python 3.12+
- Django 4.2+
- Un environnement virtuel Python

### 2️⃣ Installation

1. Clonez le projet :
   ```bash
   git clone https://github.com/AnsiLema/LitreviewFinalVersion.git
   cd LITRevu
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Sur macOS/Linux
   .venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances Python :
   ```bash
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
