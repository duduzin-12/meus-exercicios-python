from flask import Flask, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)