preço_pequena = 10
preço_media = 12
preço_grande = 15

quantidade_pequenas =int(input("Digite a quantidade de camisetas pequenas: "))
quantidade_medias =int(input("Digite a quantidade de camisetas medias: "))
quantidade_grandes =int(input("Digite a quantidade de camisetas grandes: "))

Valor_arrecadado = (quantidade_pequenas * preço_pequena) + (quantidade_medias * preço_media) +(quantidade_grandes + preço_grande)
print ("o valor total arrecadado é : ",valor_arrecadado)