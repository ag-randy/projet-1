from django.http import Http404
from django.shortcuts import render

SERVICES = [
    {
        "slug": "telephonie-mobile",
        "titre": "Téléphonie mobile",
        "resume": "Restez connecté partout avec une couverture fiable et des forfaits adaptés.",
        "description": "Digicel connecte des millions de personnes en Haïti, y compris "
                       "dans les zones reculées. Nos forfaits s'adaptent à tous les budgets "
                       "et à tous les usages, pour appeler, écrire et rester proche des "
                       "vôtres, partout dans le pays.",
    },
    {
        "slug": "internet-4g-5g",
        "titre": "Internet 4G / 5G",
        "resume": "Une connexion rapide pour naviguer, travailler et se divertir sans limites.",
        "description": "Après le premier réseau 3G du pays en 2010, nous avons lancé la 5G "
                       "en 2022. Naviguez, travaillez et diffusez en haut débit, où que "
                       "vous soyez. Une connexion pensée pour le travail, les études et "
                       "les loisirs au quotidien.",
    },
    {
        "slug": "fibre-optique",
        "titre": "Fibre optique",
        "resume": "Internet ultra rapide et stable pour la maison et les entreprises.",
        "description": "Une connexion stable et très rapide pour les foyers comme pour les "
                       "entreprises, pensée pour le télétravail, les études et le "
                       "divertissement. Elle permet de faire plusieurs choses en même "
                       "temps sans ralentissement.",
    },
    {
        "slug": "digicel-wallet",
        "titre": "Digicel Wallet",
        "resume": "Envoyez et recevez de l'argent facilement, sans compte bancaire.",
        "description": "Lancé en 2018, Digicel Wallet rend les services financiers "
                       "accessibles à tous : envoyez, recevez et payez depuis votre "
                       "téléphone, de façon simple et sécurisée. Un simple téléphone "
                       "suffit, sans compte bancaire, même loin des agences.",
    },
    {
        "slug": "television",
        "titre": "Télévision",
        "resume": "Profitez de vos programmes, films et contenus préférés en toute simplicité.",
        "description": "Retrouvez vos programmes, vos films et vos contenus préférés "
                       "dans une offre simple, directement chez vous. Une programmation "
                       "variée pour toute la famille, du divertissement à l'information.",
    },
    {
        "slug": "solutions-business",
        "titre": "Solutions Business",
        "resume": "Des outils et services pour accompagner la croissance de votre entreprise.",
        "description": "Connectivité, communication et outils numériques : nous "
                       "accompagnons les entreprises haïtiennes, des petits commerces "
                       "aux grandes structures, dans leur croissance. Notre équipe vous "
                       "conseille pour choisir les solutions adaptées à votre activité.",
    },
    {
        "slug": "fondation-digicel",
        "titre": "Fondation Digicel",
        "resume": "Nous soutenons l'éducation et les communautés à travers tout le pays.",
        "description": "Créée en 2007, la Fondation Digicel a construit plus de 60 écoles "
                       "dans les zones rurales, permettant à plus de 25 000 enfants "
                       "d'apprendre dans de bonnes conditions. Chaque année, son concours "
                       "pour jeunes entrepreneurs sélectionne 10 lauréats et distribue "
                       "plus d'un million de gourdes.",
    },
    {
        "slug": "sponsoring-evenements",
        "titre": "Sponsoring & événements",
        "resume": "Nous valorisons les talents à travers le sport et la culture haïtienne.",
        "description": "Du football aux festivals artistiques, nous soutenons les "
                       "événements qui rassemblent et font rayonner les talents haïtiens. "
                       "Nous accompagnons aussi les jeunes athlètes et les artistes vers "
                       "de nouvelles scènes.",
    },
]


def trouver_service(slug):
    for service in SERVICES:
        if service["slug"] == slug:
            return service
    return None

def index(request):
    return render(request, "index.html")

def a_propos(request):
    return render(request, "a_propos.html")

def projets(request):
    return render(request, "projets.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html", {"services": SERVICES})


def service_detail(request, slug):
    service = trouver_service(slug)
    if service is None:
        raise Http404("Ce service n'existe pas.")
    return render(request, "services_detail.html", {"service": service})