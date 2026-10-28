# Digicel Haïti — Site Vitrine

Site vitrine pour une entreprise basée en Haïti nommée "Digicel" qui évolue principalement dans la télécommunication. Ce site présente les services, 
projets et informations de contact de l'entreprise.

En utilisant Django, on l'a transformer en un app qui mpermet d'afficher des informations sans charger une nouvelle page HTML pour chacune d'elle: Services qui affiche des informations sur chacunes des services offerts a Partir de Detail Services dynamiquement.

## Aperçu
![Acceuil](static/img/Screenshot%201.png)
![A Propos](static/img/Screenshot%202.png)
![Services](static/img/Screenshot%203.png)
![Détail des Services](static/img/Screenshot%206.png)
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

## Lancer le projet en local
1. Cloner le dépôt GitHub

   ```bash
   git clone https://github.com/ag-randy/projet-1.git
   cd projet-1
   ```

2. Créer l'environnement virtuel

   ```bash
   python -m venv .venv
   ```

3. Activer l'environnement virtuel

   - Git Bash :
     ```bash
     source .venv/Scripts/activate
     ```

   - PowerShell :
     ```powershell
     .venv\Scripts\Activate.ps1
     ```

4. Installer les dépendances

   ```bash
   pip install -r requirements.txt
   ```


5. Lancer le serveur Django

   ```bash
   python manage.py runserver
   ```

6. Ouvrir le site dans un navigateur

   Accéder à http://127.0.0.1:8000/

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