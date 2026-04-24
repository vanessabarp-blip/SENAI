import math

# Recebe os catetos
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

# Calcula a hipotenusa
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# Mostra o resultado
print("O valor da hipotenusa é:", hipotenusa)