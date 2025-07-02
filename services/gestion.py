import os
import sys
from pathlib import Path

# Ajouter le dossier parent au path pour permettre les imports
sys.path.append(str(Path(__file__).parent))

try:
    from .utils import export_to_json, import_from_csv, write_log
except ImportError:
    from utils import export_to_json, import_from_csv, write_log

from dotenv import load_dotenv
load_dotenv()

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH')
EXPORT_PATH = os.getenv('EXPORT_PATH')


def students_by_city(city: str) -> list:
    """
    Args:
        city (str): The city to search for

    Returns:
        list: A list of students from the city sorted by age
    """
    students = import_from_csv(DATA_FILE_PATH)
    # Convertir l'âge en entier pour chaque étudiant
    for student in students:
        student['age'] = int(student['age'])
    
    students_city = [student for student in students if student['ville'] == city]
    students_sorted = sorted(students_city, key=lambda x: x['age'])
    write_log(f"🏙️  Récupération des étudiants de la ville {city}: {len(students_sorted)} étudiants")
    write_log(f"🏙️  {students_sorted}")

    # Export the students to a json file
    export_to_json(students_sorted, EXPORT_PATH + city + '.json')

    return students_sorted

def get_available_cities() -> list:
    """
    Returns:
        list: A list of available cities
    """
    students = import_from_csv(DATA_FILE_PATH)
    write_log(f"🏙️  Récupération des villes disponibles")
    return sorted(set(student['ville'] for student in students))


def get_cities(students: list) -> list:
    """
    Args:
        students (list): A list of students

    Returns:
        list: The lsit of all the cities for the students (used for api call optimization)
    """
    return sorted(set(student['ville'] for student in students))


if __name__ == "__main__":

    city = input("Entrez la ville à rechercher: ")
    students = students_by_city(city)