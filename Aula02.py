# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# media = float(input("Informe a média:"))
# if media > 5:
#      print("Aprovado")
# else:
#  print("Reprovado")

# for numero in [0,10,56,77,95]:
#   print(numero)
# else:
#         print("Acabou")
#         print(f'{numero}')

# for numero in range(1000000000):
#     print(numero)
#     if numero == 4:
#         break
#         print("Até mais")

# for x in [1, 10, 20, 30, 40, 50]:
#     if x == 30:
#         continue
#     print (x)

# for x in range(0, 100, 2):
#     print(x)

# for x in range(1, 100, 3):
#     print(x)

#Atividade For
# Maior = Menor = 0
# Soma = 0
#
# for x in range(11):
#     Valor = int(input("Entre com v"))
#     Soma = Soma + Valor
#     if x == 0:
#         Maior = Valor
#         Menor = Valor
#     elif x > Maior:
#         Maior = Valor
#     elif x < Menor:
#         Menor = Valor
# print(f"O maior valor é {Maior}")
# print(f"O menor valor é {Menor}")
# print(Soma)
# Media = Soma /10
# print(Media)

#Exec 1
# Soma = 0
# for x in range(10):
#     Valor = int(input("Entre com v"))
#     Soma = Soma + Valor
#     Media = Soma / 10
# print(f"A soma é {Soma}")
# print(f"A média é {Media}")

#Exec 2
# for x in range(0, 21, 2):
#     print(x)

#Exec 3
# for x in range(1, 22, 2):
#     print(x)

#Exec 4
# Soma = 0
# for x in range(0, 21, 2):
#     Soma += x
#     print(Soma)

#Exec 5
# Soma = 0
# for x in range(0, 11, 2):
#     Soma += x
#     print(Soma)

#Exec 6
# Soma = 0
# Quantidade = 10
# for x in range(Quantidade):
#     Idade = int(input("Entre com a idade"))
#     if 5 <= Idade <= 7:
#         print("A categoria é Infantil A")
#     elif 8 >= Idade <= 11:
#         print("A categoria é Infantil B")
#     elif 12 >= Idade <= 13:
#         print("A categoria é Juvenil")

# ////////////////////////////////////////////
#Atividade While

#Exec 1
# Soma = 0
# Numero = None
#
# while Numero != 0:
#     Numero = int(input("Digite um numero inteiro (0 para sair)"))
#     Soma += Numero

# print("A soma de todos os numeros informados é:", Soma)

#Exec 2
# Valor = None
# while True:
#     Numero = int(input("Digite um numero inteiro (0 para sair)"))
#
#     if Numero == 0:
#         break
#
#     if Valor is None or Numero > Valor:
#         Valor = Numero
#
# if Valor is not None:
#     print(f"O maior valor digitado foi: {Valor}")
# else:
#     print("Nenhum valor foi digitado")

#Exec 3
# Soma = 0
# Contador = 0
#
# while True:
#     Numero = int(input("Digite um numero inteiro (0 para sair)"))
#
#     if Numero == 0:
#         break
#
#     Soma += Numero
#     Contador += 1
#
#     if Contador == 0:
#         print("Nenhum numero foi digitado")
#     else:
#         Media = Soma / Contador
# print(f"Soma dos valores digitados: {Soma}")
# print(f"Media dos valores digitados: {Media}")

#Exec 4
# Soma = 0
# Numero = None
#
# while True:
#     Numero = int(input("Digite um numero inteiro (0 para sair)"))
#
#     if Numero == 0:
#         break
#
#     if Numero % 2 == 0:
#         Soma += Numero
# print(f"A soma dos valores pares é {Soma}")

#Exec 5
# Maior = 0
# Menor = 100
# Soma = 0
# Count = 0
# Idade = int(input("Entre com idade"))
# while Idade != 0:
#         Idade = int(input("Entre com idade"))
#         Soma = Soma + Idade
#         Count += 1
#         if Idade > Maior:
#             Maior = Idade
#         elif Idade < Menor:
#             Menor = Idade
# Media = Soma / Count
# print(Soma)
# print(Media)
# print(Maior)
# print(Menor)

# #Exec 6
# Num = int(input("Entre com o valor"))
# x = 0
# while x <= 10:
#     x += 1
#     print(Num * x)

#Funções
# def Soma(x, y):
#     print(x + y)
#
# Valor1 = int(input("Entre com o valor 1:"))
# Valor2 = int(input("Entre com o valor 2:"))
#
#
# Soma(Valor1, Valor2)

#/////////////////////////////////////

# def Soma(x, y):
#      print(x + y)
#
#
# def Sub(x, y):
#     print(x - y)
#
#
# def Mult(x, y):
#     print(x * y)
#
#
# def Div(x, y):
#     print(x / y)
#
# Valor1 = int(input("Entre com o valor 1:"))
# Valor2 = int(input("Entre com o valor 2:"))
#
# Soma(Valor1, Valor2)
# Sub(Valor1, Valor2)
# Mult(Valor1, Valor2)
# Div(Valor1, Valor2)