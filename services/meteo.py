import requests
import os
import sys
from datetime import datetime
from pathlib import Path

# Ajouter le dossier parent au path pour permettre les imports
sys.path.append(str(Path(__file__).parent))

try:
    from .utils import import_from_csv, export_to_json, write_log
    from .gestion import get_cities
except ImportError:
    from utils import import_from_csv, export_to_json, write_log
    from gestion import get_cities

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH')
EXPORT_PATH = os.getenv('EXPORT_PATH')

DECISION_TREE = {
    'Clear': 1,
    'Clouds': 1,
    'Rain': 0,
    'Snow': 0,
    'Thunderstorm': 0,
    'Drizzle': 0
}

TRADUCTION_WEATHER = {
    'Clear': 'Soleil',
    'Clouds': 'Nuageux',
    'Rain': 'Pluie',
    'Snow': 'Neige',
    'Thunderstorm': 'Orage',
    'Drizzle': 'Bruine'
}


def call_wheather_api(city: str) -> dict:
    """
    Args:
        city (str): The city to get the weather for

    Returns:
        dict: The weather data from the city
    """
    try:    
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        response = requests.get(url)
        write_log(f"🌤️  Appel à l'API météo pour la ville {city}: {response.json()}")
        return response.json()
    
    except Exception as e:
        write_log(f"❌ Erreur lors de l'appel à l'API météo: {e}")
        return None


def decide(student: dict, weather_data: dict | None = None) -> list:
    """
    Args:
        student (dict): The student to decide for
        weather_data (dict): The weather data for the student if already fetched

    Returns:
        str: The decision of the type of the course for the student
    """
    if weather_data is None:
        weather_data = call_wheather_api(student['ville'])

    wheather = weather_data['weather'][0]['main']

    if DECISION_TREE[wheather] == 1:
        decision = f"Cours en présentiel pour {student['nom']} ({student['ville']}) - Météo: {TRADUCTION_WEATHER[wheather]}"
    else:
        decision = f"Cours en visio pour {student['nom']} ({student['ville']}) - Météo: {TRADUCTION_WEATHER[wheather]}"
    
    write_log(f"🎓 {decision}")
    return decision


def bulk_decide(students: list) -> list:
    """
    Args:
        students (list): The students to decide for

    Returns:
        list: The decisions for the students
    """
    decisions = []

    cities = get_cities(students)
    weather_data = {}

    for city in cities:
        weather_data[city] = call_wheather_api(city)

    for student in students:
        decisions.append(decide(student, weather_data[student['ville']]))

    # Export the decisions to a json file
    export_to_json(decisions, EXPORT_PATH + 'decisions_' + city + '_' + datetime.now().strftime('%Y-%m-%d') + '.json')
    
    return decisions


if __name__ == "__main__":

    students = import_from_csv(DATA_FILE_PATH)
    decisions = bulk_decide(students)
    export_to_json(decisions, EXPORT_PATH + 'decisions_' + datetime.now().strftime('%Y-%m-%d') + '.json')


    