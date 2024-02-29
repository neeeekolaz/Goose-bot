# data_operations.py

import json
from pathlib import Path

def load_data(file_path: str):
    path = Path(file_path)
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data from {path}: {e}")
        return []

async def save_data(file_path: str, new_entry):
    path = Path(file_path)
    existing_data = load_data(path)
    existing_data.append(new_entry)
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error saving data to {path}: {e}")
