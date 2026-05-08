#exercicio 23
sua_altura = float(input("Digite sua altura : "))
sua_sombra = float(input("Digite o tamanho da sua sombra : "))
sombra_predio = float(input("Digite o tamanho da sombra do prédio : "))

altura_predio = (sombra_predio * sua_altura) / sua_sombra

print(f"Altura do prédio: {altura_predio:.2f}  em metros")