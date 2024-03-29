from threading import Thread
import time
import random


class MinhaThread(Thread):

    def __init__(self, i):
        Thread.__init__(self)
        self.i = i

    def run(self):
        time.sleep(random.randint(1, 5))
        print("Olá, agora com classe!! {}".format(self.i))


if __name__ == '__main__':

    print("Iniciando processo principal...")
    print("Criando threads...")

    threads=[]
    for a in range(10):
        t = MinhaThread(a)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Finalizando processo principal...")
