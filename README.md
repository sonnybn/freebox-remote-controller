# Freebox Remote Web

## Présentation

Ce projet propose une interface web simple permettant de contrôler un décodeur **Freebox Player** via le réseau local, en utilisant l’API HTTP intégrée à la Freebox.  
L’utilisateur peut ainsi remplacer la télécommande physique par une télécommande virtuelle accessible depuis un navigateur web.

---

## Objectifs

- Fournir une alternative fonctionnelle à la télécommande Freebox
- Expérimenter l’interaction réseau entre machines sur un LAN
- Illustrer un projet web complet avec interface HTML, serveur Flask et interaction avec des équipements tiers via API HTTP

---

## Fonctionnalités

- Interface web responsive simulant une télécommande
- Commandes de base : navigation (`up`, `down`, `left`, `right`, `ok`)
- Commandes multimédia : volume, mute, power (veille/allumage)
- Requêtes HTTP générées dynamiquement à partir des actions utilisateur

---

## Prérequis

- **Python 3.10 ou supérieur**
- Connexion locale au même réseau que la Freebox Player
- Code de la télécommande Freebox (généré par le décodeur)
- IP locale de la Freebox Player

---

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/nom-utilisateur/freebox-remote-web.git
   cd freebox-remote-web
Installer les dépendances :

pip install flask
pip install requests

Lancer le serveur :
python app.py
Accéder à l’interface :
http://localhost:5000

Configuration
1. Récupérer l’adresse IP du Freebox Player
Méthode recommandée :

Aller sur l’interface Freebox OS (via mafreebox.freebox.fr)

Accéder à la rubrique Périphériques connectés

Identifier le Freebox Player par son adresse MAC ou son nom

Sinon, depuis le terminal :
arp -a
Rechercher l’adresse IP associée à l’adresse MAC du Freebox Player

2. Récupérer le code de la télécommande
Sur la télévision (via le Player) :

Aller dans Paramètres → Système → Télécommande Freebox

Noter le code à 8 chiffres affiché (ex : 55984265)

Ce code sera utilisé dans les requêtes HTTP.

Structure du projet
freebox-remote-web/
├── app.py              # Serveur Flask
├── static/
│   └── style.css       # Styles de l’interface
├── templates/
│   └── index.html      # Interface utilisateur
└── README.md
Exemple de requête envoyée
Chaque bouton de la télécommande web génère une requête de la forme :
http://<IP_FREEBOX>/pub/remote_control?code=<CODE_TEL>&key=<TOUCHE>
Exemple pour augmenter le volume :
http://192.168.0.2/pub/remote_control?code=55984265&key=vol_up
Limitations connues
Certains codes (return, guide) ne sont pas fonctionnels selon les versions du firmware Freebox

Le comportement du bouton power dépend du contexte (veille ou allumage)

Le code de télécommande et l’adresse IP peuvent varier selon le matériel

Cas d’usage
Projet de domotique local
Présentation pédagogique sur les APIs réseau et Flask
Substitution d’une télécommande physique défaillante
Démonstration de communication client-serveur sur un réseau local

Auteurs
Projet réalisé par Sonny
Date : Avril 2025

