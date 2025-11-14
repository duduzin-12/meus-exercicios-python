from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

turma = [
  {"nome": "Ana", "nota": 8.5,},
  {"nome": "Bruno", "nota": 4.1,},
  {"nome": "Julia", "nota": 9,},
  {"nome": "Eduardo", "nota": 10,}
]

@app.route("/api/alunos")

def pegar_alunos():
  return jsonify(turma)

@app.route("/api/aluno", methods=['POST'])
def adicionar_aluno():

    dados = request.json
    
    turma.append(dados)
    
    print(f"LOG: Novo aluno adicionado: {dados}")
    
    return jsonify({"status": "sucesso", "aluno_adicionado": dados})

@app.route("/api/aluno/<string:nome>", methods=['DELETE'])
def deletar_aluno(nome):

    global turma

    turma_atualizada = [aluno for aluno in turma if aluno['nome'] != nome]

    turma = turma_atualizada

    print(f"LOG: Aluno {nome} deletado.")

    return jsonify({"status": "sucesso", "aluno_deletado": nome})

if __name__ == '__main__':
    app.run(debug=True)