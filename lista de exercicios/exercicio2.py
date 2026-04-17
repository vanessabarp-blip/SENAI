while True:
 peso = float(input("Digite o peso do prato (em kg) sem ser negativo: "))
 if peso>=0:
  break
 print("Valor Invalido")

valor_a_pagar = peso
print("O valor a pagar é de R$: ", valor_a_pagar)