'''
Escreva um programa que solicite um número ao usuário e verifique se ele é par ou ímpar.
'''
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = "é par"
else:
    resultado = "é impar"

print(f"O número {numero}  {resultado}.")