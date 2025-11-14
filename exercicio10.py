def verificar_situacao(nota):
  if nota >= 7:
    return "Aprovado."
  elif nota < 7 and nota >= 5:
    return "Em recuperação."
  else:
    return "Reprovado."
  
turma = [
  {"nome": "Ana", "nota": 8.5,},
  {"nome": "Bruno", "nota": 4.1,},
  {"nome": "Julia", "nota": 9,},
  {"nome": "Eduardo", "nota": 10,}
]

print("--- Relatório da Turma ---")

for aluno in turma:
  status = verificar_situacao(aluno['nota'])
  print(f"Nome: {aluno['nome']}; Nota: {aluno['nota']}; Situação:{status}")