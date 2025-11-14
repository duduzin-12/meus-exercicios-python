def verificar_situacao(nota):
  if nota >= 7:
    return "Aprovado."
  elif nota < 7 and nota >= 5:
    return "Em recuperação"
  else:
    return "Reprovado."
  
status_aluno1 = verificar_situacao(8.5)
status_aluno2 = verificar_situacao(6)
status_aluno3 = verificar_situacao(5.4)
status_aluno4 = verificar_situacao(4)

print(f"Aluno 1: {status_aluno1}, Aluno 2: {status_aluno2}, Aluno 3: {status_aluno3}, Aluno 4: {status_aluno4}")