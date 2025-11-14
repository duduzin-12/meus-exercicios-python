def verificar_situacao(nota):
  if nota >= 7:
    return "Aprovado."
  elif nota < 7 and nota >= 5:
    return "Em recuperação."
  else:
    return "Reprovado."
  
notas_da_turma = [8.5, 6.0, 4.0, 10.0, 5.5, 7.5, 3.0]

for nota in notas_da_turma:
  status = verificar_situacao(nota)
  print(f"Aluno com a nota {nota} está {status}")