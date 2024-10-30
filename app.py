from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import service

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('Home.html')

@app.route('/')
def index():
    partecipanti = service.get_all_partecipanti()
    return render_template('index.html', partecipanti=partecipanti)

@app.route('/partecipanti/<int:id>')
def detail(id):
    partecipante = service.get_partecipante_by_id(id)
    if partecipante is None:
        return render_template('404.html'), 404
    return render_template('detail.html', partecipante=partecipante)

@app.route('/register')
def register():
    return render_template('register.html')




@app.route('/partecipanti', methods=['GET'])
def api_get_partecipanti():
    partecipanti = service.get_all_partecipanti()
    return jsonify(partecipanti)

@app.route('/partecipanti/<int:id>', methods=['GET'])
def api_get_partecipante(id):
    partecipante = service.get_partecipante_by_id(id)
    if partecipante is None:
        return jsonify({"error": "Partecipante non trovato"}), 404
    return jsonify(partecipante)

@app.route('/partecipanti', methods=['POST'])
def api_add_partecipante():
    new_partecipante = request.get_json()
    
    if 'nome' not in new_partecipante or 'cognome' not in new_partecipante or 'email' not in new_partecipante:
        return jsonify({"error": "Dati incompleti"}), 400

    partecipante_creato = service.add_partecipante(new_partecipante)
    
    return jsonify(partecipante_creato), 201


if __name__ == '__main__':
    app.run(debug=True)