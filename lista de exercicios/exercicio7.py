horas_normais = float(input("Digite as horas normais trabalhadas: "))
horas_extras = float(input("Digite as horas extras trabalhadas: "))

salario_bruto = (horas_normais * 10) + (horas_extras * 15)

imposto = salario_bruto * 0.10

salario_liquido = salario_bruto - imposto

print("Salário bruto: R$", salario_bruto)
print("Salário líquido: R$", salario_liquido)