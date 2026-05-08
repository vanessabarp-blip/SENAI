import time

def monitorar_irrigacao():
    umidade_atual = 15
    META_IDEAL = 40
    INCREMENTO = 5
    LIMITE_SEGURANCA = 30 # Caso o sensor falhe e continue subindo
    tentativas = 0

    print("--- SISTEMA DE IRRIGAÇÃO PRO ATIVADO ---")

    while umidade_atual < META_IDEAL:
        # Simulação de segurança: impede loop infinito se a água acabar
        if tentativas > 15:
            print("ERRO: Umidade não sobe. Verifique o suprimento de água!")
            return

        print(f"[STATUS] Umidade: {umidade_atual}% | Irrigador: LIGADO")
        
        # Simula o tempo de absorção da terra
        time.sleep(0.5) 
        
        umidade_atual += INCREMENTO
        tentativas += 1

        if umidade_atual >= LIMITE_SEGURANCA:
            print("ALERTA: Umidade excessiva detectada! Desligamento de emergência.")
            break

    print(f"--- META ATINGIDA: {umidade_atual}% ---")
    print("Sistema em modo de espera (Standby).")

monitorar_irrigacao()