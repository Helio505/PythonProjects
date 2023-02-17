import json
from flask import Flask, make_response, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # para deixar em ordem alfabetica

# rota da api:
@app.route('/characters', methods=['GET'])
def get_characters():
    with open("file.json", "r") as file:
        data = json.load(file)
        file.close()

    return make_response(
        jsonify(
            message="Lista com todos os personagens salvos",
            data=data['personagens']
        )
    )

@app.route('/characters', methods=['POST'])
def create_characters():
    with open("file.json", "r") as file:
        data = json.load(file)
        file.close()
    
    personagem = request.json #request acessa o corpo da requisição
    
    with open("file.json", "w") as file:
        data['personagens'].append(personagem)
        json.dump(data, file)
        file.close()

    return(
        jsonify(
            message="Personagem salvo com sucesso",
            data=personagem
        )
    )

app.run()