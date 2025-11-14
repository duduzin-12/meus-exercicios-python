numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

somador_impar = 0

for numero in numeros:
  if not numero % 2 == 0:
    somador_impar = somador_impar + numero
  
print(f"A soma de todos os números ímpares da lista é: {somador_impar}.")