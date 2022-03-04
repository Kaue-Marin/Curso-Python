from random import randint
cont = 0
sorteio = [[]]
quants = 0
for s in range(1,61):
    sorteio = randint(1,61)
    while cont != 999:
        cont = int(input('quantos sorteios você quer fazer: '))
        quants = sorteio + 1
print(quants)