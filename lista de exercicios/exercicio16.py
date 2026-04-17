c1 = int(input("Moedas de 1 centavo: "))
c5 = int(input("Moedas de 5 centavos: "))
c10 = int(input("Moedas de 10 centavos: "))
c25 = int(input("Moedas de 25 centavos: "))
c50 = int(input("Moedas de 50 centavos: "))
r1 = int(input("Moedas de 1 real: "))

total = (c1 * 0.01) + (c5 * 0.05) + (c10 * 0.10) + (c25 * 0.25) + (c50 * 0.50) + (r1 * 1.00)

print("Total economizado: R$", total)