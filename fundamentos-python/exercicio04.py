lista_convidados = ["Ana", "Marcos", "Helena", "Jorge"]
lista_vip = ["Ana", "Marcos"]

for convidado in lista_convidados:
  if convidado in lista_vip:
    print(f"Bem-vindo(a), {convidado}! Você é VIP e pode ir para a área especial.")
  else:
    print(f"Bem-vindo(a) à festa, {convidado}.")