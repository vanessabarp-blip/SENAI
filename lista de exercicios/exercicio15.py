import math

blusas = int(input("Quantidade de blusas: "))

total_fio = blusas * 120
novelos = math.ceil(total_fio / 125)

print("Quantidade de novelos necessários:", novelos)