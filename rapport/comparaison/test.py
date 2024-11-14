import streamlit as st
import pandas as pd
import plotly.express as px
from redis_utils.fonctions_redis import *
from mongoDB_utils.fonctions_mongodb import * 


def display_test_page() : 

    # Connexion à MongoDB
    mongo_client = connexion_mongodb()
    db = mongo_client["performance_test"]
    collection = db["test_collection"]

    # Section d'introduction
    st.write("""
                Bienvenue dans cet onglet de test et de comparaison entre Redis et MongoDB. Ici, vous pourrez choisir un nombre d’enregistrements, générer un jeu de données aléatoire, 
                puis l'insérer dans les deux bases de données. Nous mesurerons les temps d'exécution pour les opérations de lecture et d'écriture dans chaque système, afin de comparer 
                leurs performances respectives et mieux comprendre les avantages et limites de chaque solution.
            """)

    # Sélection du type de test et du nombre d'entrées
    test_type = st.selectbox("Type de test", ["Écriture", "Lecture"])
    if test_type == "Écriture":
        data_type = st.radio("Types de données", ["Structurées", "Non structurées"])

    entry_counts = st.slider("Nombre d'entrées", 100, 1000, step=100)

    # Bouton pour lancer le test
    if st.button("Tester"):      

        if test_type == "Écriture":
            structured_data = generate_structured_data(entry_counts)
            data_non_structured = generate_data_non_structured(entry_counts)

            if data_type == "Structurées" : 
                st.dataframe(structured_data)
                redis_time = redis_write_test(structured_data)
                mongo_time = mongo_write_test(structured_data, collection)


            elif data_type == "Non structurées" : 
                st.dataframe(data_non_structured)
                redis_time = redis_write_test(data_non_structured)
                mongo_time = mongo_write_test(data_non_structured, collection)

        elif test_type == "Lecture":
            redis_time = redis_read_test(entry_counts) 
            mongo_time = mongo_read_test(entry_counts, collection) 

        # Créer le DataFrame
        chart_data = pd.DataFrame({
            "Temps": [redis_time, mongo_time],  
            "Base de données": ["Redis", "MongoDB"]  
        })

        # Créer le diagramme de barres avec Plotly
        fig = px.bar(chart_data, x='Base de données', y='Temps', color='Base de données',
                    title='Comparaison des Temps d\'éxecution',
                    labels={'Temps': 'Temps (ms)', 'Base de données': 'Base de données'},
                    color_discrete_sequence=["#FF0000", "#0000FF"]) 

        # Afficher le diagramme
        st.plotly_chart(fig)

        # Interprétation
        with st.expander("Interprétation"): 
            st.write("""
                     Nous observons que, pour des volumes de données faibles, Redis affiche des temps d'insertion inférieurs à ceux de MongoDB. 
                     Cependant, lorsque le nombre d'enregistrements augmente ou que les données sont non structurées, MongoDB devient plus performant 
                     que Redis pour les opérations d'écriture. Cette différence s'explique par les architectures des deux systèmes : Redis stocke les 
                     données directement en mémoire, offrant un accès ultra-rapide mais avec une persistance limitée, car les données risquent de se 
                     perdre en cas de redémarrage ou de panne. MongoDB, quant à lui, enregistre les données sur disque, assurant leur conservation 
                     permanente mais introduisant une latence due au stockage sur disque, ce qui rend généralement les accès plus lents comparé à Redis. 
                     Cependant, pour des données non structurées, MongoDB optimise les écritures en s'appuyant sur sa flexibilité de schéma, rendant l'insertion plus rapide dans ces cas.

                     En revanche, pour les opérations de lecture, quel que soit le volume des données, le temps d'exécution de Redis reste inférieur à celui de MongoDB, grâce à son stockage 
                     en mémoire qui accélère considérablement les accès.
                     """)
    

        # Conclusion
        st.subheader("Conclusion")
        st.markdown("""
                    Pour conclure, **Redis** et **MongoDB** présentent chacun des avantages distincts en matière de gestion des données, influencés par leur conception et les algorithmes de stockage qu'ils utilisent. **Redis**, avec sa structure de base en mémoire, est particulièrement adapté aux données temporaires et aux cas où la rapidité d'accès est importante. Les algorithmes de stockage en mémoire de Redis lui permettent de lire et écrire des données en millisecondes, ce qui en fait un excellent choix pour les données volatiles nécessitant un accès ultra-rapide, comme les sessions utilisateur ou les files d'attente de messages.

                    En revanche, **MongoDB**, orienté document et conçu pour le stockage persistant, excelle dans la gestion de données permanentes. Grâce à son modèle de stockage sur disque et ses algorithmes optimisés pour les opérations de lecture et écriture sur des données massives, il est idéal pour des applications nécessitant une structuration plus complexe et une conservation à long terme, comme les bases de données pour des applications analytiques ou des catalogues produits.

                    Ainsi, Redis est idéal pour les besoins de rapidité temporaire, tandis que MongoDB est préférable pour le stockage permanent et une structuration plus complexe des données. Il est également possible d'utiliser Redis et MongoDB simultanément, chaque système remplissant un rôle spécifique dans une architecture hybride. Par exemple, dans une application de livraison, Redis peut être utilisé pour suivre l'état de la commande en temps réel, tandis que MongoDB stocke les informations relatives au client et à la commande, offrant ainsi une solution performante et flexible.                 
                 """)
