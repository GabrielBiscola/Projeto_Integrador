from flask import Flask, jsonify, make_response, request
from bd import Carros

app = Flask('carros')

# Primeiro método - Visualizar dados (GET)
# app.route -> definir que essa função é uma rota para que o flask entenda que aquilo é um método que deve ser executado
@app.route('/carros', methods=['GET'])
def get_carros():
    return Carros

# Primeiro método pt.2 - Visualizar dados por ID (GET / ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carro in Carros:
        if carro.get('id') == id:
            return jsonify(carro)

# Segundo método - criar novos dados (post)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso!',
                carro=carro)
    )

# Terceiro método - Editar dados (PUT)
@app.route('/carros/<int:id>', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carros[indice].update(carro_alterado)
            return jsonify(Carros[indice])

# Quarto método - deletar dados (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def deletar_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({"mensagem:": "Carro excluído com sucesso!"})

app.run(port=5000, host="localhost")