import requests
import os
from datetime import datetime

from dotenv import load_dotenv
from utils import import_from_csv, export_to_json

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
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def decide(student: dict) -> list:
    weather_data = call_wheather_api(student['ville'])

    wheather = weather_data['weather'][0]['main']

    if DECISION_TREE[wheather] == 1:
        decision = f"Cours en présentiel pour {student['nom']} ({student['ville']}) - Météo: {TRADUCTION_WEATHER[wheather]}"
    else:
        decision = f"Cours en visio pour {student['nom']} ({student['ville']}) - Météo: {TRADUCTION_WEATHER[wheather]}"
    
    print(decision)
    return decision

if __name__ == "__main__":
    students = import_from_csv(DATA_FILE_PATH)

    decisions = []

    for student in students:
        decisions.append(decide(student))

    export_to_json(decisions, EXPORT_PATH + 'decisions_' + datetime.now().strftime('%Y-%m-%d') + '.json')


    