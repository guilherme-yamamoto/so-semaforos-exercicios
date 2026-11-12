import multiprocessing
import random
import time

#3. Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1
#sapo. Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância
#máxima para que os sapos percorram. A cada salto, um sapo pode dar um salto de 0 até o
#tamanho máximo do salto (valor aleatório entre 1 e 5 cm.). Após dar um salto, a Thread, para
#cada sapo, deve mostrar no console, qual foi o tamanho do salto e quanto o sapo percorreu.
#Assim que o sapo percorrer a distância máxima, a Thread deve apresentar a posição que
#o sapo chegou.

semaforo = None
distancia_max = random.randint(10, 30)

def init(sema, contador):
    global semaforo, posicao
    semaforo = sema
    posicao = contador

def sapo(id):
    global distancia_max
    distancia: int = 0
    while(distancia < distancia_max):
        time.sleep(1)
        salto = random.randint(0, 5)
        distancia = distancia + salto
        print(f"Sapo #{id + 1} - Salto: {salto}cm / Distância Percorrida: {distancia}/{distancia_max}cm")
    ranking(id)

def ranking(id):
    global posicao
    with semaforo:
        posicao.value += 1
    print(f"O sapo #{id + 1} chegou em {posicao.value}° lugar.")

def main():
    with multiprocessing.Manager() as manager:
        sem = multiprocessing.Semaphore(1)
        contador = manager.Value('i', 0)
        with multiprocessing.Pool(processes=5, initializer=init, initargs=(sem, contador)) as threads:
            threads.map(sapo, range(4))

if(__name__ == "__main__"):
    main()