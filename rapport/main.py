import streamlit as st
from streamlit_option_menu import option_menu
from redis_utils.redis import display_redis_page
from mongoDB_utils.mongoDB import display_mongodb_page
from comparaison.test import display_test_page

st.set_page_config(layout="wide")

# Sidebar configuration 
with st.sidebar:
    selected = option_menu("Menu", ["Accueil", "Redis", "MongoDB", "Test", "Références"], 
                           icons=["house", "server", "database", "bar-chart", "list"], 
                           menu_icon="cast", default_index=0)

st.markdown(
    """
    <h1 style='
    text-align: center;
    font-weight: bold;
    background: -webkit-linear-gradient(left, red, orange);
    background: linear-gradient(to right, red, orange);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3em;
    '>
    Base de données NoSQL
    </h1>
    """, 
    unsafe_allow_html=True
)

# Main content based on selected option
if selected == "Accueil":
    st.write("""              
        Dans un monde où la gestion des données est importante, le choix d'une base de données adaptée est essentiel pour répondre aux besoins spécifiques des entreprises. Les bases de données NoSQL, comme Redis et MongoDB, sont de plus en plus utilisées en raison de leur flexibilité et de leur capacité à traiter de grandes quantités de données.

        Cependant, l’incertitude persiste pour de nombreux utilisateurs quant à la technologie la plus adaptée à leurs besoins spécifiques, faute de ressources détaillées pour comprendre les différences. Ce rapport vise à combler cette lacune en proposant un site de tutoriel incluant des exemples de code avec Redis et MongoDB, ainsi qu’une analyse comparative de leurs performances.

        En examinant les indicateurs de performance dans divers cas d’utilisation, ce travail permettra de déterminer la solution optimale pour différents types de données, offrant ainsi un guide aux clients dans leur processus de décision.
        """)
    st.image("images/redis_vs_mongodb.jpg")

elif selected == "Redis":
    display_redis_page()

elif selected == "MongoDB":
    display_mongodb_page()

elif selected == "Test":
    st.title("Comparaison Redis vs MongoDB")
    display_test_page()

elif selected == "Références":
    st.title("Références")

    st.write("""
    Les ressources ci-dessous ont été consultées pour obtenir des informations techniques et des comparaisons détaillées entre Redis et MongoDB. Elles fournissent des bases essentielles pour comprendre les particularités et les cas d'utilisation optimaux de chaque technologie.
    """)

    st.markdown("""
    - [Documentation Redis](https://redis.io/docs/latest/operate/rc/)
    - [Documentation MongoDB](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/write-operations/#std-label-pymongo-write)
    - [IONOS](https://www.ionos.fr/digitalguide/hebergement/aspects-techniques/redis-tutoriel/)
    - [La différence entre Redis et MongoDB](https://aws.amazon.com/fr/compare/the-difference-between-redis-and-mongodb/)
    - [Streamlit](https://docs.streamlit.io/)
    """)
