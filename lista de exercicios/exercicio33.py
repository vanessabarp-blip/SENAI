# Recebe o valor do salário mínimo e do salário do funcionário
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_funcionario = float(input("Digite o salário do funcionário: "))

# Calcula quantos salários mínimos o funcionário ganha
quantidade = salario_funcionario / salario_minimo

# Mostra o resultado
print("O funcionário ganha", quantidade, "salários mínimos.")