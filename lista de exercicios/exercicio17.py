latas = int(input("Quantidade de latas (350 ml): "))
garrafas600 = int(input("Quantidade de garrafas (600 ml): "))
garrafas2L = int(input("Quantidade de garrafas (2 L): "))

total = (latas * 0.35) + (garrafas600 * 0.6) + (garrafas2L * 2)

print(f"Total de litros comprados: {total:.2f} L")