import threading
import time
import random


def imprimi(i):
    time.sleep(random.randint(1, 5))
    print("Olá Mundo - {}".format(i))


if __name__ == '__main__':
    print("Inicianod o processo")
    print("Criando thread")

    threads = []
    for a in range(10):
        t = threading.Thread(target=imprimi, args=(a,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # a = 0
    # t1 = threading.Thread(target=imprimi, args=(a,))
    #
    # t1.start()
    #
    # t1.join()
    # print("Finalizando o processo")
