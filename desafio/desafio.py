# Inicialização das variáveis
umidade_atual = 15
meta_umidade = 40
incremento = 5

print(f"Iniciando sistema... Umidade atual: {umidade_atual}%")

# Laço de incremento com verificação de teto
while umidade_atual < meta_umidade:
    print(f"Irrigador ligado... Umidade em {umidade_atual}%")
    umidade_atual += incremento  # Incrementa 5% a cada ciclo

# Mensagem final após sair do laço
print(f"Umidade final: {umidade_atual}%")
print("Nível ideal atingido.")

