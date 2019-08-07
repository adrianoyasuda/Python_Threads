import sys
import random

x = random.getrandbits(20)
print(x)

nome = sys.argv[1]

arq = open(nome, "r")

linhas = []

for l in arq.readlines():
    linhas.append(l[:-1])

print(linhas)
