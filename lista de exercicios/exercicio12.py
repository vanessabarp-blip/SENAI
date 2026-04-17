horas_normais = float(input("Horas normais trabalhadas: "))
horas_extras = float(input("Horas extras trabalhadas: "))

salario_bruto = (horas_normais * 10) + (horas_extras * 15)
salario_liquido = salario_bruto * 0.90

print("Salário bruto:", salario_bruto)
print("Salário líquido:", salario_liquido)
