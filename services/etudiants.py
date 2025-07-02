import os
from utils import export_to_json, import_from_csv
from dotenv import load_dotenv

load_dotenv()
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH')
EXPORT_PATH = os.getenv('EXPORT_PATH')

if __name__ == "__main__":

    students = []

    try:
       data = import_from_csv(DATA_FILE_PATH)
       for row in data:
           students.append(row)

    except FileNotFoundError:
        print(f"Erreur: Le fichier {DATA_FILE_PATH} n'a pas été trouvé.")
        exit(1)
    except Exception as e:
        print(f"Erreur: {e}")
        exit(1)
    
    city = input("Entrez la ville à rechercher: ")

    students_city = [student for student in students if student['ville'] == city]

    students_city = sorted(students_city, key=lambda x: x['age'])

    export_to_json(students_city, EXPORT_PATH + city + '.json')

