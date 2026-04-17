sua_altura = float(input("Digite sua altura (em metros): "))
sua_sombra = float(input("Digite o tamanho da sua sombra (em metros): "))
sombra_predio = float(input("Digite o tamanho da sombra do prédio (em metros): "))

altura_predio = (sombra_predio * sua_altura) / sua_sombra

print(f"Altura do prédio: {altura_predio:.2f} metros")