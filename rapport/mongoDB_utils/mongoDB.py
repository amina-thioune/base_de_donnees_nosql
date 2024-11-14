import streamlit as st 



def display_mongodb_page() :

    # Titre et logo 
    st.image("images/mongodb.png",  width=250)

    # Définition 
    with st.expander("Définition") :
        st.success("""
                    **MongoDB** est une base de données NoSQL orientée document qui a gagné en popularité en raison de sa flexibilité et de sa capacité à gérer des données non structurées à grande échelle. Contrairement aux bases de données relationnelles qui utilisent des tables et des lignes, MongoDB stocke les données sous forme de documents BSON (Binary JSON), permettant ainsi une structure de données plus souple et évolutive. Cela signifie que chaque document peut avoir un schéma différent, offrant une grande liberté lors de la modélisation des données.
                    
                    L'un des principaux avantages de MongoDB est sa capacité à se scalabiliser horizontalement, ce qui permet de répartir les données sur plusieurs serveurs pour gérer des volumes de trafic importants. De plus, ses fonctionnalités intégrées, telles que l'indexation, la recherche textuelle et l'agrégation, facilitent l'accès et l'analyse des données. MongoDB est couramment utilisé dans des applications web modernes, des systèmes de gestion de contenu, et des plateformes d'e-commerce, où la rapidité et l'agilité dans la gestion des données sont essentielles.      
                """ )
        
    # Installation 
    st.subheader("Installer MongoDB")
    st.code("pip install pymongo")

    # Connnexion à la base de données
    st.write("Pour vous connecter à une base de données MongoDB en cloud, allez sur le site, puis connectez-vous avec votre compte Google.")
    st.code("https://www.mongodb.com/cloud/atlas/register", language="python")   # video d'explication https://www.youtube.com/watch?v=daMxiBS0odk&t=7s&ab_channel=SAIKUMARREDDY
    st.code("""
                from pymongo import MongoClient
                client = MongoClient('mongodb+srv://username:password@mongodb.3esaj.mongodb.net/?retryWrites=true&w=majority&appName=MongoDB')  
            """, language="python")

    # Commandes de base 
    st.subheader("Quelques commandes  de base")
    with st.expander("Code") : 
        st.code("""
                    # Créer une collection
                    database = client["tp_mongodb"]
                    collection = database["test"]

                    # Insertion de documents
                    document_list = [
                        {"name": "Amina", "status": "student"},
                        {"name": "Dior", "status": "student"}
                    ]

                    # Insérer plusieurs documents dans la collection
                    result = collection.insert_many(document_list)

                    # Afficher la liste des collections
                    collections = database.list_collection_names()
                    print(collections)

                    # Compter le nombre de documents dans la collection
                    count = collection.count_documents({})
                    print("Nombre de documents:", count)

                    # Afficher tous les documents de la collection
                    find = collection.find()
                    for document in find:
                        print(document)

                    # Retourner une estimation du nombre de documents dans la collection
                    estimated_count = collection.estimated_document_count()
                    print("Estimation du nombre de documents:", estimated_count)

                    # Afficher les valeurs distinctes du champ "name"
                    distinct_names = collection.distinct("name")
                    print("Noms distincts:")
                    for name in distinct_names:
                        print(name)

                    # Modifier un champ dans un document spécifique
                    query_filter = {"name": "Amina"}
                    update_operation = {"$set": {"name": "Amy"}}
                    result_3 = collection.update_one(query_filter, update_operation)
                    print("Documents modifiés:", result_3.modified_count)

                    # Insérer un seul document dans la collection
                    result_4 = collection.insert_one({"name": "Fatou", "status": "student"})
                    print("Insertion réussie:", result_4.acknowledged)

                    # Remplacer complètement un document
                    query_filter = {"Age": "19"}
                    replace_document = {"name": "Dior", "Status": "Student", "Age": "19"}
                    result = collection.replace_one(query_filter, replace_document)
                    print("Documents remplacés:", result.modified_count)

                    # Supprimer un document
                    query_filter = {"name": "Fatou"}
                    result = collection.delete_one(query_filter)
                    print("Documents supprimés:", result.deleted_count)

                    # Supprimer la collection
                    collection.drop()
                    print("Collection supprimée.")

                    # Supprimer la base de données
                    client.drop_database('tp_mongodb')
                    print("Base de données supprimée.")
                """, language="python")
        

    # Json à MongoDB
    st.subheader("Importer un fichier JSON dans MongoDB")
    with st.expander("Code"): 
        st.code("""
                    import json

                    # Connexion à la base de données MongoDB (remplace avec tes propres paramètres)
                    database = client["database_name"]

                    def json_to_mongodb(json_file, collection_name):
                        # Charger le contenu du fichier JSON
                        with open(json_file, 'r') as f:
                            data = json.load(f)

                        # Créer une collection MongoDB
                        collection = database[collection_name]

                        # Vérifier que les données sont dans un format compatible avec MongoDB (liste ou dictionnaire)
                        if isinstance(data, dict):
                            # Si c'est un dictionnaire, insérer comme un document unique
                            collection.insert_one(data)
                        elif isinstance(data, list):
                            # Si c'est une liste de documents, insérer plusieurs documents
                            collection.insert_many(data)
                        else:
                            return "Le fichier JSON doit contenir un dictionnaire ou une liste."

                        return collection

                """, language="python")
        

    # Jointure de documents
    st.subheader("Jointures de deux documents")
    st.write("On joint deux documents dans MongoDB pour simplifier l'accès aux données en regroupant les informations en un seul document ou via des références, permettant ainsi de tout récupérer en une seule requête et de réduire le nombre d'appels. Cette approche optimise les performances en diminuant les temps de latence, notamment dans les environnements nécessitant des accès rapides, et assure la cohérence des informations, les mises à jour étant centralisées, ce qui minimise les risques d'incohérences.")
    with st.expander("Code") :
        st.code("""
                from bson.json_util import dumps

                def jointure(mc, id1, id2):
                
                    # Afficher le type de la collection MongoDB et les identifiants des documents
                    print(type(mc), id1, id2)

                    # Récupérer les documents associés aux identifiants fournis
                    doc1 = mc.find_one({'_id': id1})
                    doc2 = mc.find_one({'_id': id2})

                    # Vérifier que les deux documents existent
                    if not doc1 or not doc2:
                        return "Un ou les deux documents n'existent pas."

                    # Initialiser le dictionnaire pour stocker le résultat de la jointure
                    d_res = {}

                    # Obtenir les clés des deux documents
                    d11 = list(doc1.keys())
                    d22 = list(doc2.keys())

                    # Parcourir les clés des deux documents pour effectuer la jointure
                    for key1 in d11:
                        for key2 in d22:
                            if key1 != '_id' and key2 != '_id':  # Ignorer le champ '_id'
                                if key1 == key2:  # Si les clés sont identiques
                                    # Fusionner les valeurs des deux documents pour cette clé
                                    d_res[key1] = {**doc1[key1], **doc2[key2]}

                    # Créer un nouveau document avec le résultat de la jointure
                    jointure_doc = {'jointure_result': d_res}

                    # Insérer le document résultant de la jointure dans la collection
                    mc.insert_one(jointure_doc)

                    # Retourner le résultat de la jointure au format JSON
                    return dumps(jointure_doc)
            """, language="python")
        

    # Intersections de représentations JSON et interactions avec MongoDB
    st.subheader("Intersections de représentations JSON et interactions avec MongoDB")
    st.success("Le code suivant illustre comment effectuer une intersection entre deux documents JSON en comparant les clés communes et en fusionnant les données associées. Il permet d'insérer des documents JSON dans une collection MongoDB, de comparer les champs communs, et de sauvegarder les résultats de l'intersection. Ce processus est particulièrement utile pour combiner des données similaires issues de différents documents et les analyser efficacement dans MongoDB.")
    with st.expander("Code") : 
        st.code("""
                    import json

                    class SetEncoder(json.JSONEncoder):
                        def default(self, obj):
                            if isinstance(obj, set):
                                return list(obj)
                            return json.JSONEncoder.default(self, obj)

                    # Intersection de dictionnaires
                    def dict_intersect(*dicts):
                        comm_keys = dicts[0].keys()
                        for d in dicts[1:]:
                            # Intersecter les clés d'abord
                            comm_keys &= d.keys()
                        # Construire un dictionnaire de résultats avec compréhension imbriquée
                        result = {key: [d[key] for d in dicts] for key in comm_keys}
                        
                        res = {}
                        for key, val in result.items():
                            data_str = json.dumps(val, cls=SetEncoder)
                            res[key] = data_str

                        return res

                    # Calculer l'intersection de deux documents dans MongoDB
                    def intersection(mc, id1, id2):
                        doc1 = mc.find_one({'_id': id1})
                        doc2 = mc.find_one({'_id': id2})

                        if not doc1 or not doc2:
                            return None  # Retourner None si un des documents n'existe pas

                        d_res = {}
                        keys_doc1 = set(doc1.keys())
                        keys_doc2 = set(doc2.keys())

                        for key in keys_doc1.intersection(keys_doc2):
                            if key != '_id':
                                d_res[key] = dict_intersect(doc1[key], doc2[key])

                        result_dict = {'test': d_res}

                        # Enregistrer l'intersection dans la collection
                        mc.insert_one(result_dict)

                        return mc.find_one({'test': d_res})  # Retourner le document inséré
                """)


    # INDEX
    st.write(" ")
    st.subheader("Index 👉")
    with st.expander("Définition") :
        st.success(""" 
                    En MongoDB, un index est une structure de données spéciale qui accélère les requêtes sur certains champs en facilitant la recherche de documents. Cependant, la création et la gestion des index peuvent entraîner des coûts supplémentaires en termes de mémoire et de performances d'écriture. Un index trie les valeurs des champs spécifiés, permettant à MongoDB de localiser rapidement les documents pertinents sans devoir parcourir l'intégralité de la collection.

                    Il existe plusieurs types d'index : les index simples, les index composés, les index uniques, les index de texte, etc. Les index réduisent le nombre de documents à analyser lors d'une recherche, rendant ainsi les requêtes plus efficaces. Toutefois, les opérations d'insertion, de mise à jour et de suppression peuvent être légèrement ralenties, car MongoDB doit mettre à jour les index correspondants en parallèle des données.

                    Les index sont stockés en mémoire (RAM) pour améliorer les performances, ce qui peut augmenter l'utilisation de la mémoire si plusieurs index sont créés. Des index mal optimisés ou inutiles peuvent aussi affecter négativement les performances globales, car leur maintenance devient coûteuse en ressources.
                """)
    with st.expander("Code") : 
        st.code("""
                import csv
                import time


                def perf_mongo(csv_file, n):
                    # Connexion à MongoDB
                    client = connexion_mongodb()
                    mydb = client["mydatabase"]
                    mycol = mydb["mycollection"]

                    # Vider la collection existante
                    mycol.drop()

                    # Lire le fichier CSV pour déterminer la première colonne
                    with open(csv_file, encoding='utf-8') as csvfile:
                        my_reader = csv.DictReader(csvfile, delimiter='\t')
                        first_row = next(my_reader)
                        
                        # Créer un index basé sur la première colonne
                        index_field = list(first_row.keys())[0]
                        mycol.create_index([(index_field, 1)])

                    # Lire les données du fichier CSV et convertir en dictionnaires
                    with open(csv_file, encoding='utf-8') as csvfile:
                        my_reader = csv.DictReader(csvfile, delimiter='\t')
                        my_data = [my_row for my_row in my_reader]

                    # Évaluer la performance en mesurant le temps de traitement
                    st = time.process_time()
                    for my_row in my_data[:n]:
                        # Insérer ou mettre à jour le document basé sur la première colonne
                        mycol.replace_one({index_field: my_row[index_field]}, my_row, upsert=True)
                    et = time.process_time()
                    
                    # Calcul du temps d'exécution
                    res = et - st
                    duplicates = n - mycol.count_documents({})
                    
                    return {
                        'execution_time': res,
                        'duplicates_found': duplicates
                    }
                """)

    # Agregation
    st.write(" ")
    st.subheader("Agrégation")
    with st.expander("Définition") : 
        st.success("""L'**agrégation** est une méthode pour traiter et analyser les données en regroupant, filtrant, et transformant des documents directement dans la base de données. 
                   Elle utilise un "pipeline d'agrégation," qui est une série d'étapes appliquées aux données, comme filtrer avec `$match`, regrouper avec `$group`, et trier avec `$sort`. 
                   Cela permet de réaliser des calculs comme les totaux et les moyennes sans devoir extraire les données. Par exemple, on peut facilement calculer le total des ventes par 
                   produit en regroupant les données et en appliquant une somme, ce qui rend MongoDB très efficace pour les analyses directement en base.""")

    with st.expander("Exemple d'application") : 
        st.code("""
                   # Collection de documents représentant des ventes de produits
                    [
                        { "produit": "Livre", "quantité": 10, "prix": 15 },
                        { "produit": "Stylo", "quantité": 25, "prix": 2 },
                        { "produit": "Livre", "quantité": 5, "prix": 15 },
                        { "produit": "Stylo", "quantité": 15, "prix": 2 }
                    ]

                    # Définition du pipeline d'agrégation pour calculer les ventes totales par produit
                    pipeline = [
                        {
                            # Étape $group : Regrouper les documents par le champ "produit"
                            "$group": {
                                "_id": "$produit",  
                                "ventes_totales": {
                                    # Calculer la somme des ventes pour chaque produit
                                    "$sum": {
                                        # Multiplier "quantité" et "prix" pour obtenir le total de chaque vente
                                        "$multiply": ["$quantité", "$prix"]
                                    }
                                }
                            }
                        }
                    ]

                    # Exécuter le pipeline d'agrégation sur la collection MongoDB
                    result = collection.aggregate(pipeline)

                    # Résultat attendu : Liste de documents avec le produit et le total des ventes
                    [
                        { "_id": "Livre", "ventes_totales": 225 },  
                        { "_id": "Stylo", "ventes_totales": 80 }   
                    ]

                """)
        