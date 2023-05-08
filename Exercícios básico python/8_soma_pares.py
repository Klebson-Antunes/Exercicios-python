'''
Escreva um programa que solicite uma lista de números ao usuário e exiba a soma dos números pares da lista.
'''
# Declara uma lista vazia
lista_numeros = []

# Solicita ao usuário a quantidade de numeros que deseja inserir na lista
quantidade_numeros = int(input("Quantos números deseja inserir na lista? "))

# inicializa a variavel soma_pares
soma_pares = 0

# cria um loop para solicitar os numeros e inserir na lista
for i in range(quantidade_numeros):
    # Entrada de dados do usuário
    numero = int(input(f"Digite o {i+1} número: "))
    # add a lista de numeros
    lista_numeros.append(numero)
    
    # verifica os numeros pares para realizar a soma
    if lista_numeros[i] % 2 == 0:
        soma_pares += lista_numeros[i]

# Exibe o resultado
print(f"O resultado da soma de números pares = {soma_pares}.")