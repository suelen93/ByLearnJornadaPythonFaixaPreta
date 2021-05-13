#Cria uma calculadora básica

print('Seja bem vindo(a)!')
print()

print('Digite um número correspondente a opção desejada:')
operacao = int(input('1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão => '))


if operacao == 1:
  print()
  valor1 = float(input('Insira o 1º valor: '))
  valor2 = float(input('Insira o 2º valor: '))

  soma = valor1 + valor2

  print()
  print(f'{valor1} + {valor2} = {soma}')

elif operacao == 2:
  print()
  valor1 = float(input('Insira o 1º valor: '))
  valor2 = float(input('Insira o 2º valor: '))

  subtracao = valor1 - valor2

  print()
  print(f'{valor1} - {valor2} = {subtracao}')

elif operacao == 3:
  print()
  valor1 = float(input('Insira o 1º valor: '))
  valor2 = float(input('Insira o 2º valor: '))

  multiplicacao = valor1 * valor2

  print()
  print(f'{valor1} * {valor2} = {multiplicacao}')

elif operacao == 4:
  print()
  valor1 = float(input('Insira o 1º valor: '))
  valor2 = float(input('Insira o 2º valor: '))

  divisao = valor1 / valor2

  print()
  print(f'{valor1} / {valor2} = {divisao}')
