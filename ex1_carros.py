import multiprocessing
import time
import random

#chegada: int = 0
#saida: int = 0
semaforo = None

def init(sema):
    #global chegada
    #global saida
    global semaforo
    #chegada = cheg
    #saida = sai
    semaforo = sema

def direcao_origem():
    sentido_int = random.randint(1, 4)
    sentido_str = ""

    if(sentido_int == 1):
        sentido_str = "Norte"
    elif(sentido_int == 2):
        sentido_str = "Sul"
    elif(sentido_int == 3):
        sentido_str = "Leste"
    elif(sentido_int == 4):
        sentido_str = "Oeste"
    return sentido_str

def direcao_sentido():
    orientacao_int = random.randint(1, 4)
    orientacao_str = ""

    if(orientacao_int == 1):
        orientacao_str = "Norte"
    elif(orientacao_int == 2):
        orientacao_str = "Sul"
    elif(orientacao_int == 3):
        orientacao_str = "Leste"
    elif(orientacao_int == 4):
        orientacao_str = "Oeste"
    return orientacao_str

def carro_andando(id):
    origem = direcao_origem()
    print(f"\033[31mCHEGANDO NO CRUZAMENTO: Carro #{id} / Origem -> {origem}\033[0m")
    #print()

def carro_parado(id):
    print(f"\033[33mCARRO ESPERANDO CRUZAMENTO: Carro #{id}\033[0m")
    #print()

def carro_passando(id):
    destino = direcao_sentido()
    print(f"\033[32mCARRO PASSANDO: Carro #{id} / Destino -> {destino}\033[0m")
    #print()

def carro(id):
    global semaforo
    time.sleep(random.uniform(0.1, 2.0))

    carro_andando(id)       ##Independente
    carro_parado(id)        ##Independente

    with semaforo:      
        carro_passando(id)  ##Seção Crítica
        time.sleep(random.uniform(0.8, 1.2))

def main():
    sem = None

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=10, initializer=init, initargs=(sem,)) as threads:
            threads.map(carro, range(10))

if(__name__ == "__main__"):
    main()