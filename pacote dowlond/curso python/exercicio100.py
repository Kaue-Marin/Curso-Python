from random import randint
numeros = []
def sorteia():
    for c in range(1, 5):
        c = randint(1, 9)
        numeros.append(c)
    print(f'os valores da lista são {numeros}')
def somapar():
    spar = 0
    for c2 in numeros:
        if c2 % 2 == 0:
            spar += c2
    print(f'a soma dos numeros pares é {spar}')
# programa principal
sorteia()
somapar()