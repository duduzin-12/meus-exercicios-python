class ContaBancaria:
  def __init__(self, titular):
    self.titular = titular
    self.saldo = 0

  def depositar(self, valor):
    try:
      valor_convertido = float(valor)
      self.saldo += valor_convertido
      return f"Depositado R${valor_convertido:.2f} com sucesso."
    except (ValueError, TypeError):
      return "[ERROR] Use números, não use letras."
  
  def sacar(self, valor):
    try:
      valor_convertido = float(valor)
      if self.saldo >= valor_convertido:
        self.saldo -= valor_convertido
        return f"Saque de R${valor_convertido:.2f} liberado."
      else:
        return "[ERROR] Saldo insuficiente."
    except (ValueError, TypeError):
      return "[ERROR] Use números, não use letras."
    
  def extrato(self):
    return f"O saldo da conta de {self.titular} é de R${self.saldo:.2f}"

eduardo = ContaBancaria(titular="Eduardo")
print(eduardo.sacar(100))
print(eduardo.depositar(500))
print(eduardo.sacar(45))
print(eduardo.sacar(600))
print(eduardo.extrato())

opcao = input("Deseja (d)epositar, (s)acar ou sair?").lower()

while opcao != "sair":
  if opcao == "d" or opcao == "D":
    valor_deposito = input("Digite o valor do depósito: ")
    print(eduardo.depositar(valor_deposito))
  elif opcao == "s" or opcao == "S":
    valor_saque = input("Digite o valor que deseja sacar: ")
    print(eduardo.sacar(valor_saque))
  else:
    print("Letra inválida, utilize apenas d ou s")

  print(eduardo.extrato())
  opcao = input("Deseja (d)epositar, (s)acar ou sair?").lower()

print("Sistema finalizado.")