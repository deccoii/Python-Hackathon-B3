import argparse
import os
import sys
from datetime import datetime
from typing import List, Dict

from services.gestion import students_by_city, get_available_cities
from services.meteo import bulk_decide, call_wheather_api, DECISION_TREE, TRADUCTION_WEATHER
from services.utils import export_to_json, write_log

from dotenv import load_dotenv
load_dotenv()

# Configuration
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH')
EXPORT_PATH = os.getenv('EXPORT_PATH')
REPORT_PATH = os.getenv('REPORT_PATH')

def process_city(city: str):
    """
    Process a city
    """
    students = students_by_city(city)
    return {
        'city': city,
        'students': students,
        'decisions': bulk_decide(students)
    }


def process_all_cities():
    """
    Process all cities
    """
    results = []
    for city in get_available_cities():
        results.append(process_city(city))
    return results


def generate_report(results: list):
    """
    Generate a report
    """
    nb_cities = len(results)
    nb_visio = 0
    nb_presentiel = 0
    for result in results:
        for decision in result['decisions']:
            if 'visio' in decision.lower():
                nb_visio += 1
            else:
                nb_presentiel += 1
    report = f"🏙️  {nb_cities} villes traitées\n"
    report += f"🏙️  {nb_visio} cours en visio\n"
    report += f"🏙️  {nb_presentiel} cours en présentiel\n"
    
    with open(f"{REPORT_PATH}report_{datetime.now().strftime('%Y-%m-%d')}.txt", 'w', encoding='utf-8') as file:
        file.write(report)
    
    write_log(f"🏙️  Rapport généré: {REPORT_PATH}report_{datetime.now().strftime('%Y-%m-%d')}.txt")


def main():
    """Fonction principale avec interface CLI"""

    # Configuration argparse
    parser = argparse.ArgumentParser(
        description="🎓 Gestion des étudiants et organisation des cours selon la météo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python main.py --city Paris                    # Traiter une ville spécifique
  python main.py --full                          # Traiter toutes les villes
  python main.py --full --report                 # Mode complet avec rapport
  python main.py --list-cities                   # Afficher les villes disponibles
        """
    )
    
    parser.add_argument(
        '--city', '-c',
        type=str,
        help='Nom de la ville à traiter'
    )
    
    parser.add_argument(
        '--full', '-f',
        action='store_true',
        help='Traiter automatiquement toutes les villes'
    )
    
    parser.add_argument(
        '--report', '-r',
        action='store_true',
        help='Générer un rapport de synthèse (utilisé avec --full)'
    )
    
    parser.add_argument(
        '--list-cities', '-l',
        action='store_true',
        help='Afficher la liste des villes disponibles'
    )

    args = parser.parse_args()
    
    write_log("🎓 Démarrage de l'application de gestion des cours")
    
    try:
        # Vérifier si le fichier de données existe
        if not DATA_FILE_PATH or not os.path.exists(DATA_FILE_PATH):
            write_log(f"❌ Fichier de données non trouvé: {DATA_FILE_PATH}")
            return 1
        
        # Liste des villes
        if args.list_cities:
            cities = get_available_cities()
            print("🏙️  Villes disponibles:")
            for city in cities:
                print(f"   • {city}")
            return 0
        
        # Mode automatique complet
        if args.full:
            results = process_all_cities()
            
            if args.report:
                generate_report(results)
            
            print(f"\n✅ Traitement terminé pour {len(results)} ville(s)")
            return 0
        
        # Traitement d'une ville spécifique
        if args.city:
            cities = get_available_cities()
            
            # Vérifier si la ville existe
            if args.city not in cities:
                print(f"❌ Ville '{args.city}' non trouvée.")
                print(f"Villes disponibles: {', '.join(cities)}")
                write_log(f"❌ Ville '{args.city}' non trouvée.")
                return 1
            
            result = process_city(args.city)
            
            if result['students']:
                print(f"\n✅ Traitement terminé pour {args.city}")
                print(f"📊 {result['stats']['total']} étudiant(s) traité(s)")
                write_log(f"✅ Traitement terminé pour {args.city}")
                write_log(f"📊 {result['stats']['total']} étudiant(s) traité(s)")
            else:
                print(f"❌ Aucun étudiant trouvé pour {args.city}")
                write_log(f"❌ Aucun étudiant trouvé pour {args.city}")
            
            return 0
        
        # Mode interactif si aucun argument
        cities = get_available_cities()
        print("🏙️  Villes disponibles:", ", ".join(cities))
        
        while True:
            city = input("\n🔍 Entrez le nom de la ville à traiter (ou 'quit' pour quitter): ").strip()
            
            if city.lower() in ['quit', 'q', 'exit']:
                print("👋 Au revoir !")
                break
            
            if not city:
                print("❌ Veuillez entrer un nom de ville.")
                continue
            
            if city not in cities:
                print(f"❌ Ville '{city}' non trouvée.")
                continue
            
            result = process_city(city)
            print(f"✅ Traitement terminé pour {city}")
            print(f"📊 {result['stats']['total']} étudiant(s) traité(s)")
            write_log(f"✅ Traitement terminé pour {city}")
            write_log(f"📊 {result['stats']['total']} étudiant(s) traité(s)")
        
        return 0
        
    except KeyboardInterrupt:
        write_log("👋 Application interrompue.")
        return 0
    except Exception as e:
        write_log(f"❌ Erreur fatale: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
