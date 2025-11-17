#1- Crie uma função chamada calculadora_divisao(a, b). A função deve tentar dividir a por b.

#2- Tratamento 1: Se o usuário mandar um texto em vez de número (ex: "dez"), o Python vai dar TypeError ou ValueError. Use try/except para capturar isso e retornar "Erro: Digite apenas números".

#3- Tratamento 2: Se o usuário tentar dividir por zero (ex: 10 / 0), o Python dá ZeroDivisionError. Capture isso e retorne "Erro: Não é possível dividir por zero".

#4- Se der tudo certo, retorne o resultado.

def calculadora(a, b):
  try:
    a_convertido = float(a)
    b_convertido = float(b)
    resultado = a_convertido / b_convertido
    return f"{resultado:.2f}"
  except ZeroDivisionError:
    return "[ERROR] Não é possível dividir por 0."
  except ValueError:
    return "[ERROR] Não use letras, use apenas números."
  
a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")

print(calculadora(a, b))