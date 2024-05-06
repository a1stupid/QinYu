import json

def load_json(path):
    with open(path, encoding='UTF-8') as f:
        return json.load(f)

def save_json(path):
    pass