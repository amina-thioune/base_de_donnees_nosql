import time
from pymongo import MongoClient
import random


def connexion_mongodb() :

    # Remplacer Usernane et password 
    client = MongoClient('mongodb+srv://username:password@mongodb.3esaj.mongodb.net/?retryWrites=true&w=majority&appName=MongoDB')
    return client


# Fonction pour écrire des données dans MongoDB
def mongo_write_test(data, collection):
    
    start_time = time.time()
    collection.insert_many([{"key": i, "value": value} for i, value in enumerate(data)])
    return time.time() - start_time


# Fonction pour lire des données dans MongoDB
def mongo_read_test(num_entries, collection):
    client = connexion_mongodb()
    start_time = time.time()
    for i in range(num_entries):
        _ = collection.find_one({"_id": i})
    end_time = time.time()
    return end_time - start_time


# Générateur de données non structurées 
def generate_data_non_structured(num_entries):

    """Génère des données non structurées sous forme de mémos et notes."""
    memos_and_notes = [
        "Finaliser la présentation du projet pour la réunion de lundi.",
        "Note : Examiner les nouvelles règles de conformité avant le prochain audit.",
        "Mémorandum : La prochaine réunion d'équipe est programmée pour le 5 novembre à 10h.",
        "Note rapide : Les chiffres de ventes du troisième trimestre montrent une augmentation de 15%.",
        "À faire : Contacter le service client pour discuter des retours récents.",
        "Note : Mettre à jour le budget avec les dernières projections financières.",
        "Mémo : Revue de performance du logiciel prévue pour la fin du mois.",
        "Observation : Les clients montrent un intérêt croissant pour les produits de la gamme écologique.",
        "Note : Vérifier les mises à jour de sécurité pour tous les serveurs.",
        "Mémorandum : Présentation de la nouvelle politique de télétravail à l'équipe.",
    ]

    # Génération de données non structurées pour le nombre d'entrées spécifié
    data = [random.choice(memos_and_notes) for _ in range(num_entries)]
    return data
