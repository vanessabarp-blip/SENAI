nome = input("insira o nome do aluno")
nota1 = float(input ("insira a primeira média"))
nota2 =float(input ("insira a segunda média"))
media = (nota1 + nota2)/2
print("A média das notas é :" ,media)
if media>= 7: 
  print("O aluno esta aprovado")  
else:
  print("O aluno esta reprovado")
  