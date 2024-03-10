import time

def tombamento_safra(path):
    print("Iniciando tombamento da safra...")
    yield "Iniciando tombamento da safra..."
    time.sleep(2)  # Simulação de trabalho
    
    print("Arquivo", path, "tombado com sucesso!")
    yield "Arquivo " + path + " tombado com sucesso!"
    time.sleep(1)
    
    print("Finalizando tombamento da safra...")
    yield "Finalizando tombamento da safra..."

    for i in range(1, 101, 1):
        print(i)
        yield f"{str(i)}"
        time.sleep(1)

    #return messages