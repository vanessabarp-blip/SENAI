qtd1 = int(input("Moedas de 1 centavo: "))
qtd5 = int(input("Moedas de 5 centavos: "))
qtd10 = int(input("Moedas de 10 centavos: "))
qtd25 = int(input("Moedas de 25 centavos: "))
qtd50 = int(input("Moedas de 50 centavos: "))
qtd1real = int(input("Moedas de 1 real: "))

total = (qtd1 * 0.01) + (qtd5 * 0.05) + (qtd10 * 0.10) + \
        (qtd25 * 0.25) + (qtd50 * 0.50) + (qtd1real * 1.00)

print(f"Total economizado: R$ {total:.2f}")