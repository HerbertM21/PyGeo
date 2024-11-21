import json
import os

def get_exams_by_category(categoria: str) -> list:
    """
    Obtiene los exámenes de una categoría específica desde el archivo JSON.
    """
    json_path = os.path.join('resources', 'data', 'exams.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            exams = json.load(file)
            return exams.get(categoria, [])
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {json_path}")
        return []