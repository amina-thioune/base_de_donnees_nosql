import streamlit as st
import redis 
from redis_utils.fonctions_redis import * 



def display_redis_page() : 

    # Titre et logo 
    st.image("images/redis.png",  width=250)

    # Définition
    with st.expander("Définition"):
        st.error("""            
                    Les **bases de données NoSQL** représentent une catégorie de systèmes de gestion de bases de données conçus pour gérer des volumes massifs de données non structurées ou semi-structurées. Contrairement aux bases de données relationnelles qui reposent sur des tables et des schémas rigides, les bases de données NoSQL offrent une flexibilité accrue, permettant de stocker des données sous diverses formes telles que des documents, des colonnes, des paires clé-valeur ou des graphes. Elles sont particulièrement adaptées aux applications nécessitant une scalabilité horizontale, une haute disponibilité et des performances optimisées.

                    **Redis** est l'un des exemples les plus populaires de base de données NoSQL. Initialement conçu comme un store en mémoire, Redis propose une structure de données clé-valeur extrêmement rapide, supportant des types variés tels que des chaînes, des listes, des ensembles et des hashmaps. Grâce à sa rapidité et à sa simplicité d'utilisation, Redis est souvent utilisé pour des cas d'utilisation tels que la mise en cache, la gestion des sessions et la gestion des files d'attente. En explorant Redis, nous mettons en lumière les avantages des bases de données NoSQL dans le paysage actuel des applications, ainsi que les fonctionnalités uniques qui font de Redis un outil incontournable pour les développeurs.
        """)

    st.subheader("Installer Redis")
    st.code("pip install redis") 

    st.subheader("Connexion à la base de données")
    st.write("Pour vous connecter à la base de données, visitez le site de Redis Cloud 	👇, créez une nouvelle base de données et récupérez vos informations de connexion")
    st.code("https://cloud.redis.io/#/")

    st.code("""
    r = redis.Redis(
        host='*****',  # Remplacez par le host fourni par le service cloud
        port=17931,
        password='******'  # Remplacez par le mot de passe fourni par le service cloud
    )
    """) 

    # Commandes de bases
    st.subheader("Quelques commandes de base")
    with st.expander("Codes") : 
        st.code(""" 
                    # Ajouter un ou plusieurs paires clé-valeur
                    r.set('key1', 'value1')
                    r.mset({'key2': 'value2', 'key3': 'value3'})

                    # Modifier un ou plusieurs clés existantes
                    r.set('key2', 'new_value2')
                    r.mset({'key1': 'new_value1', 'key3': 'new_value3'})

                    # Récupérer un ou plusieurs valeurs
                    r.get('key1')
                    r.mget(['key1', 'key2', 'key3'])

                    # Ajouter des éléments dans une liste
                    r.rpush('mylist', 'element1', 'element2', 'element3')

                    # Ajouter des éléments dans un ensemble
                    r.sadd('myset', 'value1', 'value2', 'value3')

                    # Supprimer des clés
                    r.delete('key1', 'key2')

                    # Supprimer un élément d'une liste
                    r.lrem('mylist', 0, 'element1')

                    # Supprimer un élément d'un ensemble
                    r.srem('myset', 'value1')

                    # Vérifier si une clé existe
                    r.exists('key1')

                    # Obtenir toutes les clés
                    r.keys('*')

                    # Effacer la base de données Redis
                    r.flushdb()

                """)


    # Convertir un fichier csv en json
    st.subheader("Convertir le fichier CSV en JSON")
    st.write("La conversion d'un fichier CSV en JSON pour Redis permet de bénéficier d'une meilleure compatibilité et flexibilité, car JSON est idéal pour stocker des structures de données complexes sous forme de paires clé-valeur. Cela facilite également l'intégration avec d'autres systèmes, notamment les applications web et les APIs.")

    with st.expander("Code") : 
        st.code(""" 
                    import csv
                    from json import dumps

                    def csv_to_json(csv_file, json_file):
                        # Créer un dictionnaire
                        data_dict = {}
                        csv_rows = []
                        # Ouvrir un fichier CSV
                        with open(csv_file, encoding='latin1', newline='') as csv_file_handler:
                            csv_reader = csv.DictReader(csv_file_handler)
                            field = csv_reader.fieldnames
                            for row in csv_reader:
                                # Ajouter chaque ligne du CSV sous forme de dictionnaire
                                csv_rows.extend([{field[i]: row[field[i]] for i in range(len(field))}])

                        data_dict['test'] = csv_rows

                        # Convertir le dictionnaire en chaîne JSON
                        json_data = dumps(data_dict, ensure_ascii=False, indent=4)

                        # Écrire les données JSON dans un fichier
                        with open(json_file, 'w', encoding='utf-8') as json_file_handler:
                            json_file_handler.write(json_data)

                        return json_file
                """) 
        

    # Jointure des objets json 
    st.subheader("Joindre deux fichiers json")
    st.write("Joindre deux fichiers JSON avant de les insérer dans Redis permet de consolider les données en une seule structure, évitant leur dispersion et facilitant leur gestion. Cela optimise les requêtes en réduisant le besoin de multiples appels pour récupérer des informations liées, tout en assurant la cohérence des opérations, les données étant disponibles ensemble et sans risque de désynchronisation. Au final, cela rend les opérations dans Redis plus rapides et efficaces.")
    with st.expander("Code") : 
        st.code(""" 
                    from json import loads, dumps
                
                    def jointure(json1, json2, join_key):
                        # Charger les deux JSON en tant que dictionnaires
                        d1 = loads(json1)['data']
                        d2 = loads(json2)['data']
                        
                        d_res = []
                        
                        # Itérer à travers les deux ensembles de données pour la jointure
                        for item1 in d1:
                            for item2 in d2:
                                if item1[join_key] == item2[join_key]:  # Comparer les valeurs de la clé commune
                                    joint_dict = {**item1, **item2}  # Fusionner les deux dictionnaires
                                    d_res.append(joint_dict)

                        # Générer la chaîne JSON finale avec la jointure
                        final_result = {'jointure': d_res}
                        return dumps(final_result, ensure_ascii=False, indent=4)
                """)


    # convertir un fichier json en une base de données
    st.subheader("Importer un fichier JSON dans Redis") 
    with st.expander("Code"):
        st.code("""
                    import json
                    import redis

                    def json_to_redis(json_file):
                        # Charger le contenu du fichier JSON
                        with open(json_file, 'r') as f:
                            data = json.load(f)

                        # Récupérer les éléments sous 'test'
                        items = data.get('test', {})

                        # Insérer les données dans Redis
                        if isinstance(items, dict):
                            for key, value in items.items():
                                r.set(key, json.dumps(value))
                        else:
                            return "Le contenu sous 'test' n'est pas un dictionnaire."

                        # Récupérer les données depuis Redis et les retourner
                        return {key: json.loads(r.get(key)) for key in items.keys() if r.get(key)}
                """)
    
    st.write("")
    # Bloom Filter
    st.header("BLOOM FILTER 🔎") # 🔍
    with st.expander("Définition") :
        st.error("""
                    Un **Bloom filter** est une structure de données efficace en mémoire qui permet de tester si un élément 
                    appartient à un ensemble, avec la possibilité de faux positifs mais jamais de faux négatifs. Il est 
                    souvent utilisé pour économiser des ressources lors de recherches rapides. Avec Redis, via l'extension 
                    **RedisBloom**, on peut utiliser des Bloom filters pour vérifier rapidement si des éléments sont présents 
                    dans des ensembles massifs, ce qui aide à réduire les requêtes coûteuses en mémoire ou en temps de calcul.

                """)

    # connexion à redisbloom
    st.subheader("Connexion à RedisBloom")
    st.code("""
            from redisbloom.client import Client
            rb = Client(host='******', 
                        port=17931, 
                        password='*****')
            """)



