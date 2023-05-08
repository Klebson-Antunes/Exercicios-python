'''
Escreva um programa que solicite dois números ao usuário e exiba a soma,
a subtração, a multiplicação e a divisão desses números.

'''
numero1 = int(input("Digite o 1° número: "))
numero2 = int(input("Digite o 2° número: "))
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} * {numero2} = {multiplicacao}")
print(f"{numero1} / {numero2} = {round(divisao, 2)}") # insere 2 casas decimais