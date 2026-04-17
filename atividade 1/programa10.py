contador = 1
soma  =  0
while contador <= 5:
  salario=float(input(f"Digite o salario do {contador}funcionário"))
  contador+= 1
  soma += salario
media = soma / 5
print ("A media dos salarios dos 5 funcionarios é: ",media)
