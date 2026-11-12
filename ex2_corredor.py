import multiprocessing
import time
import random

#2. Quatro pessoas caminham, cada uma em um corredor diferente. Os 4 corredores terminam
#em uma única porta. Apenas 1 pessoa pode cruzar a porta, por vez. Considere que cada
#corredor tem 200m. e cada pessoa anda de 4 a 6 m/s. Cada pessoa leva de 1 a 2 segundos
#para abrir e cruzar a porta. Faça uma aplicação que simule essa situação.

semaforo = None
velocidade: int = 0

def init(sema):
    global semaforo
    semaforo = sema

def pessoa(id):
    lista: str = [0]*10
    lista = ["Colevati", "Guilherme", "Satoshi", "Paulo", "Midiã", "Mario", "Luciano", "Herman", "Marcos", "Jessica"]
    nome = lista[random.randint(0, 9)]
    
    velocidade = random.randint(4, 6)
    chegada(nome, velocidade)

    with semaforo:   
        porta(nome)

def chegada(id, velocidade):
    distancia = 200
    tempo = distancia / velocidade

    time.sleep(tempo / 10)
    print(f"Pessoa {id} chegou na porta.")

def porta(id):
    passar_porta = random.randint(1, 2)
    time.sleep(passar_porta)
    print(f"Pessoa {id} entrou.")

def main():
    sem = None

    with multiprocessing.Manager() as gerenciador:
        sem = gerenciador.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem,)) as threads:
            threads.map(pessoa, range(4))

if(__name__ == "__main__"):
    main()