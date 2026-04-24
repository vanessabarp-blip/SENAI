# Salário do João
salario = 1200.00

# Valores das contas
c1 = 200.00
c2 = 120.00

# Calcula multa de 2% para cada conta
c1_com_multa = c1 * 1.02
c2_com_multa = c2 * 1.02

# Calcula total gasto
total_contas = c1_com_multa + c2_com_multa

# Calcula o restante do salário
restante = salario - total_contas

# Mostra o resultado
print("Valor pago na C1 com multa:", c1_com_multa)
print("Valor pago na C2 com multa:", c2_com_multa)
print("Total gasto:", total_contas)
print("Restante do salário:", restante)