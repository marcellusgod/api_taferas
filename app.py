from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tarefas = [
    {
        'id': '0',
        'responsavel': 'Saldanha',
        'tarefa': 'Desenvolver método GET',
        'status': 'concluido'
    },
    {
        'id': '1',
        'responsavel': 'Marcelo',
        'tarefa': 'Desenvolver método POST',
        'status': 'pedente'
    }
]

@app.route('/tarefas/<int:id>', methods=['GET','PUT','DELETE'])
def _tarefa(id):
    if request.method == 'GET':
        tarefa = tarefas[id]
        print(tarefa)
        return jsonify(tarefa)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        dados = tarefas[id].pop()

@app.route('/tarefas/', methods=['POST','GET'])
def listar_tarefas():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(tarefas)
        dados['id'] = posicao
        tarefas.append(dados)
        return jsonify(tarefas[posicao])
    elif request.method == 'GET':
        return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)