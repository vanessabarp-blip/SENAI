# Recebe o número do usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Mostra a tabuada de 1 a 10
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)