import math

# Entrada de dados
diametro = float(input("Digite o diâmetro da caixa (em metros): "))
altura = float(input("Digite a altura da caixa (em metros): "))
raio = diametro / 2
volume = math.pi * (raio ** 2) * altura
print(f"O volume da caixa d'água é: {volume:.2f} metros cúbicos")