# Digicel Haïti — Site Vitrine

Site vitrine pour une entreprise basée en Haïti nommée "Digicel" qui évolue principalement dans la télécommunication. Ce site présente les services, 
projets et informations de contact de l'entreprise.

En utilisant Django, on l'a transformer en un app qui mpermet d'afficher des informations sans charger une nouvelle page HTML pour chacune d'elle: Services qui affiche des informations sur chacunes des services offerts a Partir de Detail Services dynamiquement.

## Aperçu
![Acceuil](static/img/Screenshot%201.png)
![A Propos](static/img/Screenshot%202.png)
![Services](static/img/Screenshot%203.png)
![Détail des Services](static/img/Screenshot%203.png)
![Projets](static/img/Screenshot%204.png)
![Contact](static/img/Screenshot%205.png)


## Technologies
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- JavaScript
- Django 6.1.2
- Pas de base de données mais l'utilisation d'une liste Python dans `views.py` dont chacun constitue un dictionnaire.

## Fonctionnalités
- Navigation et menu responsive optimisée pour mobile, tablette et ordinateur.
- Effet machine à écrire sur le hero
- Animations au scroll
- Formulaire de contact avec validation
- Bouton back-to-top
- Transition fluide entre les pages
- Pages générées depuis une liste de données Python pour afficher les services offerts par l'entreprise
- Page d'erreur 404 si le service n'existe pas


## Lancer en local
1. Aller sur le lien https://github.com/ag-randy/projet-1.git
2. Cloner le repo 
3. Créer l'environnement virtuel `python -m venv .venv` (ou n'importe quel nom vous voulez nommer l'environnement à la place de env)
3. L'activer: `.venv\Scripts\Activate` pour Git Bash ou `.venv\Scripts\Activate` pour PowerShell 
4. Installer les dépendances depuis `requirements.txt`
5. Lancer le serveur: `python manage.py run server`
6. Ouvre l'addresse http://... dans votre navigateur

## Structure
```
projet-1/
├── manage.py          
├── requirements.txt    
├── .gitignore           
├── config/             
│   ├── settings.py      
│   └── urls.py          
├── vitrine/             
│   ├── views.py         
│   └── urls.py          
├── templates/           
│   ├── base.html        
│   ├── index.html      
│   ├── a_propos.html
│   ├── services.html    
│   ├── services_detail.html  
│   ├── projets.html
│   └── contact.html
└── static/              
    ├── css/style.css    
    ├── js/script.js     
    └── img/             
```


## Auteur
GUERRIER Randy Anderson — https://github.com/ag-randy