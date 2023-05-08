'''
Escreva um programa que solicite uma lista de números ao usuário e exiba a média dos números.
'''

# Declara uma lista vazia
lista_numeros = []

# Solicita ao usuário a quantidade de numeros que deseja inserir na lista
quantidade_numeros = int(input("Quantos números deseja inserir na lista? "))

# inicia a variavel soma
soma = 0

# cria um loop para solicitar os numeros e inserir na lista
for i in range(quantidade_numeros):
    # Entrada de dados do usuário
    numero = int(input(f"Digite o {i+1} número: "))
    # add a lista de numeros
    lista_numeros.append(numero)
    
    #soma dos numeros
    soma += lista_numeros[i]
    
# calcula a media
media = soma / len(lista_numeros)

# exibe o resultado
print(f"A média da soma dos numeros = {media}")

