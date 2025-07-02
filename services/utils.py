import json
import csv
import os
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

LOG_DIR = os.getenv('LOG_DIR', 'logs/')

def write_log(message):
    with open(f"{LOG_DIR}{datetime.now().strftime('%Y-%m-%d')}.log", 'a', encoding='utf-8') as file:
        file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] - {message}\n")

def import_from_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            write_log(f"🏙️  Importation des étudiants depuis le fichier {file_path}")
            return list(reader)
        
    except FileNotFoundError:
        write_log(f"❌ Le fichier {file_path} n'a pas été trouvé.")

    except Exception as e:
        write_log(f"❌ Erreur lors de l'importation des étudiants: {e}")

def export_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
        write_log(f"🏙️  Exportation des étudiants vers le fichier {file_path}")