'''
Escreva um programa que solicite um número ao usuário e verifique se ele é positivo, negativo ou zero.
'''
numero = int(input("Digite um número: "))
'''
if numero > 0:
    resultado = "é positivo"
elif numero < 0:
    resultado = "é negativo"
else:
    resultado = "é zero"

Refatorando para operador ternario
'''
resultado = "é positivo" if numero > 0 else "é negativo" if numero < 0 else "é zero"

print(f"O número {numero} {resultado}.")