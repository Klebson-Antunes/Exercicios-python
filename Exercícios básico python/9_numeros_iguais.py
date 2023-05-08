'''
Escreva um programa que solicite uma lista de números ao usuário e verifique se todos os números são iguais.
'''
# Declara uma lista vazia
lista_numeros = []

# Solicita ao usuário a quantidade de numeros que deseja inserir na lista
quantidade_numeros = int(input("Quantos números deseja inserir na lista? "))
cont = 1
# cria um loop para solicitar os numeros e inserir na lista
for i in range(quantidade_numeros):
    # Entrada de dados do usuário
    numero = int(input(f"Digite o {i+1} número: "))
    # add a lista de numeros
    lista_numeros.append(numero)
    

# Verifica se todos os números são iguais
if all(x == lista_numeros[0] for x in lista_numeros):
    print("Todos os números da lista são iguais.")
else:
    print("A lista contém números diferentes.")