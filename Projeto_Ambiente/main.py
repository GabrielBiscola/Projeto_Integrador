from bd import Campos
from flask import Flask, jsonify, make_response, request

app = Flask('ambiente')


# Mostrar amostras do ambiente
@app.route('/ambiente', methods=['GET'])
def get_campos():
    return Campos

# Mostrar amostra especifica por id
@app.route('/ambiente/<int:id>', methods=['GET'])
def get_campos_id(id):
    for amostra in Campos:
        if amostra.get('id') == id:
            return jsonify(amostra)

# Criar nova amostra
@app.route('/ambiente', methods=['POST'])
def criar_amostra():
    amostra = request.json
    Campos.append(amostra)
    return make_response(
        jsonify(mensagem="Nova amostra cadastrada!",
                amostra=amostra)
    )

# Editar amostra
@app.route('/ambiente/<int:id>', methods=['PUT'])
def editar_amostra(id):
    amostra_editada = request.get_json()
    for indice, amostra in enumerate(Campos):
        if amostra.get('id') == id:
            Campos[indice].update(amostra_editada)
            return jsonify(Campos[indice])

# Deletar amostra
@app.route('/ambiente/<int:id>', methods=['DELETE'])
def deletar_amostra(id):
    for indice, amostra in enumerate(Campos):
        if amostra.get('id') == id:
            del Campos[indice]
            return jsonify({"mensagem": "Amostra deletada com sucesso!"})

app.run(port=5000, host="localhost")