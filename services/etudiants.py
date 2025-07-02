import csv
from utils import export_to_json

DATA_FILE_PATH = 'data/etudiants.csv'
EXPORT_PATH = 'exports/'

if __name__ == "__main__":

    etudiants = []

    try:
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file: 
            reader = csv.DictReader(file)

            for row in reader:
                etudiants.append(row)

    except FileNotFoundError:
        print(f"Erreur: Le fichier {DATA_FILE_PATH} n'a pas été trouvé.")
        exit(1)
    except Exception as e:
        print(f"Erreur: {e}")
        exit(1)
    
    ville = input("Entrez la ville à rechercher: ")

    etudiants_ville = [etudiant for etudiant in etudiants if etudiant['ville'] == ville]

    etudiants_ville = sorted(etudiants_ville, key=lambda x: x['age'])

    export_to_json(etudiants_ville, EXPORT_PATH + ville + '.json')

