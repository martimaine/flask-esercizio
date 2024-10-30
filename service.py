import json

def load_data():
    with open('db.json', 'r') as f:
        return json.load(f)

def save_data(data):
    with open('db.json', 'w') as f:
        json.dump(data, f, indent=4)

def get_all_partecipanti():
    return load_data()

def get_partecipante_by_id(id):
    partecipanti = load_data()
    return next((p for p in partecipanti if p['id'] == id), None)

def add_partecipante(new_partecipante):
    partecipanti = load_data()
    
    new_id = max(p['id'] for p in partecipanti) + 1 if partecipanti else 1
    new_partecipante['id'] = new_id
    
    partecipanti.append(new_partecipante)
    save_data(partecipanti)
    
    return new_partecipante