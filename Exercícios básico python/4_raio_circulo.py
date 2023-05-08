'''
Escreva um programa que solicite o raio de um círculo ao usuário e calcule sua área e perímetro.
'''
import math

raio = float(input("Digite o raio do círculo: "))

area = math.pi * (raio ** 2)

perimetro = 2 * math.pi * raio

print(f"A área do círculo de raio {raio:.2f} é {area:.2f}")
print(f"O perímetro do círculo de raio {raio:.2f} é {perimetro:.2f}")