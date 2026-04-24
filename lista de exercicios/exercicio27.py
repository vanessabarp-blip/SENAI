# Recebe o salário fixo e o valor das vendas
salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor das vendas: "))

# Calcula a comissão (4%)
comissao = vendas * 0.04

# Calcula o salário final
salario_final = salario_fixo + comissao

# Mostra os resultados
print("Comissão:", comissao)
print("Salário final:", salario_final)