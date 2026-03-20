num_pao = int(input("Digite a quantidade de pães vendidos:"))
num_broas = int(input("Digite a quantidade de broas vendidas:"))

arrecadado = (num_pao * 0.12) + (num_broas * 1.50)
poupança = (arrecadado * 0.10)

print("Total de vendas de pães e broas  foi de :" ,arrecadado)
print("A quantidade de dinheiro que ira para a poupança:" ,poupança)