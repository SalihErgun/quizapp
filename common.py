import json
import os

def load_json(file_path):
    """JSON dosyasını yükler ve içeriklerini döndürür."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(file_path, data):
    """Verilen veriyi JSON dosyasına kaydeder."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)



