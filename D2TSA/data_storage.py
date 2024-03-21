import json
import os

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding = 'utf-8') as file:
            json.dump(data, file, ensure_ascii = False, indent = 4)
        print(f'Data successfully saved to {filename}')
    except Exception as e:
        print(f'Error saving data to {filename}: {e}')

def load_from_json(filename):
    if not os.path.exists(filename):
        print(f'No file found at {filename}')
        return None

    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f'Error loasing data from {filename}: {e}')
        return None

def append_to_json(data, filename):
    existing_data = load_from_json(filename) or []
    if isinstance(existing_data, list):
        existing_data.append(data)
    else:
        existing_data = [existing_data, data]

    save_to_json(existing_data, filename)