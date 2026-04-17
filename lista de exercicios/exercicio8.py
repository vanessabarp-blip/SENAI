numero = int(input("Digite um número até 3 dígitos: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print("CENTENA =", centena)
print("DEZENA =", dezena)
print("UNIDADE =", unidade)