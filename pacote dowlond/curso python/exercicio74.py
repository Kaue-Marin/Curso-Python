maior = 0
menor = 0
from random import randint
# 1 gerar 5 valores aleatorios
for c in range (1,6):
    n = randint(0,100)
# 2 guarda 5 valores numa tupla
    print(n, end=' ')
# 3 mostrar os numeros do maior para o menor
# 4 mostrar o menor numero
    if n > maior:
        maior = n
    if c == 1:
        menor = n
    else:
        if n < menor:
            menor = n
# 5 mostrar maior numero
print('\n' 'o maior numero é', maior)
print('o menor numero é', menor)