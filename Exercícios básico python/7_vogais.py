'''
Escreva um programa que solicite uma frase ao usuário e conte o número de vogais na frase.
'''
frase = input("Digite uma frase: ")

# Define uma Lista com as vogais
vogais = ["a", "e", "i", "o", "u"]

# Inicializa a contagem de vogais
num_vogais = 0

# Percorre cada caractere da frase
for letra in frase:
     # verifica se a letra é uma vogal(Ignorando Maiúsculas e minúsculas)
     if letra.lower() in vogais:
         num_vogais += 1
         
# Exibe o resultado
print(f" A frase contém {num_vogais} vogais.")