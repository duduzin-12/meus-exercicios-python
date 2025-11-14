numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

contador_de_pares = 0

for numero in numeros:
  if numero % 2 == 0:
    contador_de_pares += 1
    print(f"Número: {numero}, Contador de pares: {contador_de_pares}")
  else:
    print(f"Número: {numero}, Impar.")

print(f"Total de pares: {contador_de_pares}")