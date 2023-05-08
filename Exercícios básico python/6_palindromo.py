'''
Escreva um programa que solicite uma palavra ao usuário e verifique se é um palíndromo
(ou seja, se pode ser lida de trás para frente).
'''
palavra = input("Digite uma palavra: ")

# Inverte a palavra
palavra_invertida = palavra[:: -1]

# Verifica se é um palíndromo
if palavra == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")