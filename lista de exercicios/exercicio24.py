# Recebe as duas notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média ponderada (peso 2 e 3)
media = (nota1 * 2 + nota2 * 3) / (2 + 3)

# Mostra o resultado
print("A média ponderada é:", media)