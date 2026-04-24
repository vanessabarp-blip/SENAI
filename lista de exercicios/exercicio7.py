salario = float(input("Digite o salário atual: "))

salario_aumentado = salario * 1.15
imposto = salario_aumentado - imposto
salario_final = salario_aumentado * 0.92

print("Salário inicial:", salario)
print("Salário com aumento:", salario_aumentado)
print("Salário final:", salario_final)
