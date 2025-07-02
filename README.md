# 🎓 Hackathon ESGI - Gestion des Étudiants et Cours selon Météo

**Projet Python DevOps** - Module Scripting Python  
**Objectif :** Solution légère pour la gestion automatique des étudiants et l'organisation des cours selon les conditions météorologiques.

## 📋 Description du Projet

Ce projet implémente une solution complète pour le Campus Eductive permettant de :
- **Gérer automatiquement** les listes d'étudiants par ville
- **Générer des statistiques** simples sur les cours
- **Décider automatiquement** du mode de cours (présentiel/visioconférence) selon la météo
- **Sauvegarder** toutes les données importantes en JSON
- **Générer des rapports** de synthèse

### 🌤️ Logique Météorologique
- **Cours en présentiel** : Temps clair (`Clear`) ou nuageux (`Clouds`)
- **Cours en visioconférence** : Pluie (`Rain`), neige (`Snow`), orage (`Thunderstorm`), bruine (`Drizzle`)

## 🚀 Installation et Configuration

### 1. Prérequis
- **Python 3.7+**
- **Clé API OpenWeatherMap** (gratuite sur [openweathermap.org](https://openweathermap.org/api))
- **Connexion internet** pour l'API météo

### 2. Installation du Projet

```bash
# Cloner le projet
git clone <votre-repo>
cd Python-Hackathon-B3

# Créer et activer l'environnement virtuel
python -m venv venv

# Activation selon votre OS :
source venv/bin/activate      # Linux/Mac
# ou
venv\Scripts\activate         # Windows

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Configuration Environnement

Créez un fichier `.env` à la racine du projet :

```env
# Clé API OpenWeatherMap (OBLIGATOIRE pour la météo)
WEATHER_API_KEY=votre_cle_api_openweathermap

# Chemins des fichiers
DATA_FILE_PATH=data/etudiants.csv
EXPORT_PATH=exports/
REPORT_PATH=reports/

# Configuration des logs
LOG_DIR=logs/
```

### 4. Vérification de l'Installation

```bash
# Test rapide sans API météo
python main.py --list-cities

# Si vous voyez la liste des villes, l'installation est correcte !
```

## 💻 Utilisation de l'Application

### 🔧 Interface CLI (Ligne de Commande)

#### Commandes Principales

```bash
# Afficher toutes les villes disponibles
python main.py --list-cities
python main.py -l

# Traiter une ville spécifique
python main.py --city Paris
python main.py -c Lyon

# Mode automatique - traiter toutes les villes
python main.py --full
python main.py -f

# Mode complet avec génération de rapport
python main.py --full --report
python main.py -f -r

# Aide complète
python main.py --help
```

#### Exemples d'Utilisation CLI

**Exemple 1 : Traitement d'une ville**
```bash
python main.py --city Marseille
```
Résultat :
- Filtre les étudiants de Marseille
- Appelle l'API météo pour Marseille
- Décide du mode de cours selon la météo
- Affiche les décisions pour chaque étudiant
- Sauvegarde dans `exports/marseille.json`

**Exemple 2 : Traitement complet avec rapport**
```bash
python main.py --full --report
```
Résultat :
- Traite automatiquement toutes les villes
- Génère un rapport global dans `reports/report_YYYY-MM-DD.txt`
- Sauvegarde toutes les décisions dans `exports/decisions_YYYY-MM-DD.json`

### 🖥️ Mode Interactif

Si vous lancez l'application sans arguments :

```bash
python main.py
```

L'application passe en **mode interactif** :
- Affiche automatiquement toutes les villes disponibles
- Vous demande de saisir une ville à traiter
- Permet de traiter plusieurs villes successivement
- Tapez `quit`, `q`, ou `exit` pour quitter

## 📁 Structure du Projet

```
Python-Hackathon-B3/
├── 📁 data/
│   └── etudiants.csv              # Données des étudiants (nom, âge, email, ville)
├── 📁 exports/                    # Fichiers JSON générés
│   ├── paris.json                 # Étudiants filtrés par ville
│   ├── lyon.json
│   └── decisions_YYYY-MM-DD.json  # Décisions météo globales
├── 📁 reports/                    # Rapports de synthèse
│   └── report_YYYY-MM-DD.txt      # Statistiques globales
├── 📁 logs/                       # Logs quotidiens
│   └── YYYY-MM-DD.log             # Journal d'activité du jour
├── 📁 services/                   # Modules métier
│   ├── __init__.py                # Package Python
│   ├── gestion.py                 # 📊 Gestion des étudiants
│   ├── meteo.py                   # 🌤️ API météo et décisions
│   └── utils.py                   # 🔧 Fonctions utilitaires
├── main.py                        # 🚀 Interface CLI principale
├── requirements.txt               # 📦 Dépendances Python
├── .env                           # ⚙️ Configuration (à créer)
├── .gitignore                     # Git ignore
└── README.md                      # 📖 Documentation
```

## 🎯 Fonctionnalités Implémentées

### ✅ Partie 1 - Gestion des Utilisateurs
- [x] Demande de ville à l'utilisateur (CLI + mode interactif)
- [x] Filtrage des étudiants par ville
- [x] Tri des étudiants par âge croissant
- [x] Sauvegarde en JSON : `exports/<ville>.json`

### ✅ Partie 2 - Organisation des Cours selon Météo
- [x] Appel API OpenWeatherMap pour chaque ville
- [x] Décision automatique présentiel/visioconférence
- [x] Messages formatés pour chaque étudiant
- [x] Génération du fichier : `exports/decisions_<date>.json`

### ✅ Partie 3 - Structure Logicielle
- [x] **gestion.py** : Fonctions liées aux étudiants
- [x] **meteo.py** : Appel API et logique météo
- [x] **main.py** : Exécution principale avec CLI
- [x] **utils.py** : Fonctions utilitaires
- [x] Paramètres dans fichier `.env`
- [x] Système de logs quotidiens dans `logs/`

### ✅ Partie Bonus
- [x] **Interface CLI complète** avec argparse
- [x] Option `--full` pour traitement automatique
- [x] **Génération de rapport.txt** avec statistiques :
  - Nombre de villes traitées
  - Nombre d'étudiants en visio
  - Nombre d'étudiants en présentiel
- [x] **Mode interactif** sans arguments

## 📊 Système de Logs Personnalisé

### Fonctionnalités
- **Fichier quotidien** : `logs/YYYY-MM-DD.log`
- **Timestamp automatique** sur chaque entrée
- **Niveaux** : INFO, WARNING, ERROR, DEBUG
- **Historique automatique** par jour

### Format des Logs
```
[2024-12-07 14:30:15] - 🎓 Démarrage de l'application de gestion des cours
[2024-12-07 14:30:16] - 🏙️ Traitement de la ville: Paris
[2024-12-07 14:30:17] - 📊 3 étudiant(s) trouvé(s) à Paris
[2024-12-07 14:30:18] - 🌤️ Météo à Paris: Nuageux
[2024-12-07 14:30:19] - 🎓 Mode de cours: présentiel
```

## 🛠️ Exemples Complets d'Utilisation

### Scénario 1 : Traitement Manuel d'une Ville
```bash
python main.py --city Paris
```
**Sortie attendue :**
```
Cours en présentiel pour Thibault Renaud (Paris) – Météo : Nuageux
Cours en présentiel pour Claudine Gilles (Paris) – Météo : Nuageux
Cours en présentiel pour Vincent-Laurent Klein (Paris) – Météo : Nuageux

✅ Traitement terminé pour Paris
📊 3 étudiant(s) traité(s)
```

### Scénario 2 : Traitement Automatique Complet
```bash
python main.py --full --report
```
**Résultat :**
- Traite toutes les villes automatiquement
- Génère `reports/report_2024-12-07.txt` :
```
🏙️  9 villes traitées
🏙️  12 cours en visio
🏙️  18 cours en présentiel
```

### Scénario 3 : Mode Interactif
```bash
python main.py
```
**Session interactive :**
```
🏙️  Villes disponibles: Bordeaux, Lille, Lyon, Marseille, Nantes, Nice, Paris, Toulouse

🔍 Entrez le nom de la ville à traiter (ou 'quit' pour quitter): Lyon
[Traitement de Lyon...]
✅ Traitement terminé pour Lyon

🔍 Entrez le nom de la ville à traiter (ou 'quit' pour quitter): quit
👋 Au revoir !
```

## 🔧 Développement et Tests

### Tests Rapides
```bash
# Test sans API météo
python main.py --list-cities

# Test avec une ville (nécessite clé API)
python main.py --city Paris

# Test des modules individuellement
python services/gestion.py
python services/meteo.py
```

### Structure des Données

**Fichier CSV d'entrée** (`data/etudiants.csv`) :
```csv
nom,age,email,ville
Thérèse Laroche,23,rousseloceane@live.com,Marseille
Agathe-Alix Faure,22,alfred43@de.fr,Nantes
```

**Fichier JSON de sortie** (`exports/paris.json`) :
```json
[
  {
    "nom": "Thibault Renaud",
    "age": 22,
    "email": "smonnier@laposte.net",
    "ville": "Paris"
  }
]
```

## 🐛 Dépannage

### Erreurs Communes

**❌ "Fichier de données non trouvé"**
- Vérifiez que `data/etudiants.csv` existe
- Vérifiez le chemin dans le fichier `.env`

**❌ "ModuleNotFoundError"**
- Activez l'environnement virtuel : `source venv/bin/activate`
- Installez les dépendances : `pip install -r requirements.txt`

**❌ Erreur API météo**
- Vérifiez votre clé API dans `.env`
- Vérifiez votre connexion internet
- Vérifiez que votre quota API n'est pas dépassé

### Logs de Débogage
Consultez les logs quotidiens dans `logs/YYYY-MM-DD.log` pour diagnostiquer les problèmes.

## 📝 Configuration Avancée

### Variables d'Environnement Complètes
```env
# API (OBLIGATOIRE pour la météo)
WEATHER_API_KEY=your_openweathermap_api_key

# Chemins personnalisables
DATA_FILE_PATH=data/etudiants.csv    # Fichier CSV des étudiants
EXPORT_PATH=exports/                 # Dossier exports JSON
REPORT_PATH=reports/                 # Dossier rapports
LOG_DIR=logs/                        # Dossier logs quotidiens
```

### Personnalisation
- Modifiez `DECISION_TREE` dans `services/meteo.py` pour changer la logique météo
- Ajoutez des traductions dans `TRADUCTION_WEATHER`
- Personnalisez les formats de logs dans `services/utils.py`

## 🎓 Conformité au Cahier des Charges

### Technologies Utilisées
- **Python 3.7+** avec modules standard
- **API OpenWeatherMap** pour la météo
- **argparse** pour l'interface CLI
- **JSON/CSV** pour les données
- **dotenv** pour la configuration
- **Logs personnalisés** (sans module logging)

