# Aminata THIOUNE   Groupe Augias
# Compte Rendu : Cours de Bases de Données Avancées

Ce dépôt contient le compte rendu de notre cours de Bases de Données Avancées, avec une application développée avec Streamlit pour analyser Redis et MongoDB et comparer leurs performances. Le projet inclut également des scripts et des jeux de données pour tester les différentes fonctions.


## Répertoires du Projet

- **rapport/** : contient le compte rendu du projet, les analyses de résultats, et les conclusions.
- **script/** : contient les scripts Python pour les opérations sur Redis et MongoDB.
  - `redis.py` : script pour les manipulations de données sur Redis.
  - `mongo.py` : script pour les manipulations de données sur MongoDB.

- **data/** : fichiers de données utilisés dans les scripts pour tester les différentes fonctions.


## Structure de l'Application

L'application comprend les pages suivantes :

- **Accueil** : introduction à l'objectif du compte rendu et aperçu des bases de données étudiées.
- **Redis** : documentation sur Redis, incluant une définition, des instructions de connexion, des commandes de base, et des exemples de manipulations de données possibles.
- **MongoDB** : documentation sur MongoDB, avec une définition, des étapes de connexion, des commandes de base, et des manipulations de données illustrées.
- **Test** : comparaison des performances entre Redis et MongoDB, avec des tests d'écriture et de lecture.
- **Références** : liste des ressources et documents de référence utilisés pour le rapport.


## Configuration de Connexion

Pour exécuter l'application et les scripts, vous devez vous connecter à Redis Cloud et MongoDB Cloud. Suivez ces étapes :

1. **Connexion à Redis Cloud** :
   - Créez un compte sur [Redis Cloud](https://app.redislabs.com/).
   - Récupérez les informations de connexion (hôte, port, mot de passe).
   - Ajoutez ces informations dans la section de connexion du script `redis.py` et dans la page `fonctions_redis` de l'application.

2. **Connexion à MongoDB Cloud** :
   - Créez un compte sur [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
   - Créez un cluster et récupérez les informations de connexion (URI).
   - Ajoutez ces informations dans la section de connexion du script `mongo.py` et dans la page `fonctions_mongodb` de l'application.


## Installation et Exécution

Pour exécuter l'application en local :

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/amina-thioune/base_de_donnees_nosql.git
    ```

2. Accédez au répertoire du projet :
    ```bash
    cd rapport
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Lancez l'application :
    ```bash
    streamlit run main.py
    ```

