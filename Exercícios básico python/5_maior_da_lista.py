'''
Escreva um programa que solicite uma lista de números ao usuário e exiba o maior e o menor número da lista.
'''
lista_numeros = []
quantidade_numeros = int(input("Quantos números você quer digitar? "))


# Loop para solicitar a entrada de numeros e armazenar na lista_numeros
for i in range(quantidade_numeros):
    numero = int(input(f"Digite {i+1} numero(s): "))
    lista_numeros.append(numero)
  
    
# Encontra o maior e menor número da lista_numeros
maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

# Exibir resultado

print(f"O maior número é {maior_numero}")
print(f"O menor número é {menor_numero}")