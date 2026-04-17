dias = int(input("Digite a quantidade de dias: "))

anos = dias // 365
resto = dias % 365

meses = resto // 30
dias_restantes = resto % 30

print(anos, "anos,", meses, "meses e", dias_restantes, "dias")