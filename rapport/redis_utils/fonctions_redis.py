import streamlit as st 
import json
from json import loads, dumps
import time 
import random 
import string



# connexion à la base de données rédis 
def connexion_redis() :

    # Remplacer host et password
    import redis

    r = redis.Redis(
    host='********',
    port=17931,
    password='*******')

    # Vérifier la connexion
    try:
        r.ping() 
        return r
    except redis.ConnectionError:
        st.error("Échec de la connexion à Redis")
        return None 
    
# Fonction pour écrire des données dans Redis
def redis_write_test(data):

    r = connexion_redis()
    start_time = time.time()
    for i in range(len(data)):
        # Convertir chaque entrée en chaîne JSON
        r.set(f"key_{i}", json.dumps(data[i]))  

    return time.time() - start_time


# Fonction pour lire les données dans Redis
def redis_read_test(num_entries):
    r = connexion_redis()
    start_time = time.time()
    for i in range(num_entries):
        _ = r.get(f"key_{i}")
    end_time = time.time()
    return end_time - start_time



# Générateur de données structurées : dictionnaires JSON
def generate_structured_data(num_entries):
    
    structured_data = []
    for i in range(num_entries):
        entry = {
            "id": i,
            "name": f"User_{i}",
            "email": f"user_{i}@example.com",
            "age": random.randint(18, 65),
            "address": {
                "street": f"{random.randint(1, 999)} Main St",
                "city": random.choice(["Paris", "Lyon", "Marseille"]),
                "zipcode": "".join(random.choices(string.digits, k=5))
            }
        }
        structured_data.append(entry)
    return structured_data
