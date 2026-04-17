import time

tempo = 10  

while tempo > 0:
    print(f"Tempo restante: {tempo} segundos")
    time.sleep(1)  
    tempo -= 1
print("Tempo finalizado. Pode abrir a prensa.")
