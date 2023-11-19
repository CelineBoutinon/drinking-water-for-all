![dwfa_logo_small](https://github.com/CelineBoutinon/drinking-water-for-all/assets/143210563/ee97b7f1-f822-4134-a8f4-317eae1629cb)



# FAIRE UNE ETUDE SUR L'EAU POTABLE AVEC POWER BI

Projet realisé en octobre 2023 dans le cadre de ma formation Data Analyst avec OpenClassrooms.

## Objectif du projet

L’ONG DWFA (Drinking Water For All) a pour ambition de donner accès à l’eau potable à tout le monde au travers de 3 domaines d’expertise :
- Création de services d’accès à l’eau potable ;
- Modernisation de services d’accès à l’eau déjà existants ; et
- Consulting auprès d’administrations/gouvernements à propos des politiques d’accès à l’eau.

L’association a effectué une demande de financement auprès d’un bailleur de fonds en présentant ces 3 domaines d’expertise. Ces nouveaux financements, s’ils sont accordés par le bailleur, pourront permettre d’investir dans un des domaines d’expertise dans un pays qui n’est pas encore déterminé.

Dans ce cadre, l'objectif de la mission est de:
- réaliser un tableau de bord présentant une vue globale de l’accès à l’eau potable dans le monde. Celui-ci permettra de choisir le pays à cibler dès que le bailleur de fonds aura donné sa réponse sur le domaine d’expertise qu’il souhaite financer; et
- décrire les étapes préalables à l'élaboration de ce tableau de bord (mock-up et blueprint).

Plusieurs sources publiques de données ont été utilisées pour compléter les données de départ, en particulier concernant la méthodologie de collecte et de reporting des données et la méthodologie de calcul de certains indicateurs (comme l'indice de stabilité politique par exemple):
- le site de l'OMS : https://www.who.int/
- le site de la FAO : https://www.fao.org/faostat/en/#home
- le site de la Banque Mondiale : https://www.worldbank.org/en/home



## Liste des dossiers & fichiers
***
* **dossiers :**
  - **donnees-brutes :** fichiers téléchargés depuis les sources (format .xlsx et .csv)
  - **donnees-nettoyees :** fichiers prêts à alimenter la base (format .csv)
 


* **fichiers :**
	- **blueprint.pdf :** tableau de synthese des indicateurs par vue et par domaine d'expertise
	- **creation_script.sql :** script de création de la base et des tables avec la fonction Forward Engineer de MySQL Workbench
  - **dashboard.pbix :** tableau de bord réalisé avec Power BI Desktop
  - **data_prep.ipynb :** code Python permettant l'import des fichiers .csv, leur nettoyage et l'export vers la base de données MySQL (également au format .py)
  - **functions.py :** repertoire generique de fonctions a certaines desquelles le Notebook Jupyter fait appel
  - **mockup.pdf :** planches de visualisation des indicateurs presents dans le blueprint (="storyboard")
  - **schema.mwb :** schéma relationnel de la base MySQL
	- **presentation.pdf :** diapositives de présentation du projet
  - **presentation_notes.pdf :** notes d’accompagnement des diapositives de présentation du projet
  - **schema.mwb :** schema de la base dans MySQL (aussi au format .png)


## Compétences développées
* Créer le schéma d'une base de données
* Créer des tables dans une base de données
* Charger des données dans une base de données
* Effectuer des operations CRUD avec un client Python
* Analyser un besoin client pour formuler des questions analytiques
* Créer un tableau de bord répondant à des questions analytiques
* Générer des graphiques adaptés aux types de données
* Synthétiser des résultats à destination d'un client



## Langages & software
* MySQL / MySQL Workbench
* Python / Pandas / NumPy / MissingNo / MySQL Connector
* Power BI / PowerQuery
* Jupyter Notebook








