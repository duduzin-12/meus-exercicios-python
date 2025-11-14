produto = {
  "nome": "Camiseta",
  "preco": 79.90,
  "em_estoque": True
}

produto["cor"] = "Azul"

for chave, valor in produto.items():
  print(f"{chave}: {valor}")
