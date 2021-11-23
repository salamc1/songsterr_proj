import json

def read_raw_json(filename='data.json'):
    with open(filename) as f:
        data = json.load(f)

    return data
