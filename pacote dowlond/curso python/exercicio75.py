# 1 ler 4 valores
from operator import index


tot9 = 0
totpar = 0
a = int(input('digite um numero: '))
b = int(input('digite um numero: '))
c = int(input('digite um numero: '))
d = int(input('digite um numero: '))
tupla = (a,b,c,d)
for c in tupla:
# 2 guarda-los em uma tupla
# 3 mostrar quantas vezes apareceu 9
    if c == 9:
        tot9 += 1
# 4 mostrar em que posição apareceu 3
# 5 quais foram os numeros pares
    if c%2==0:
        totpar += 1
if 3 in tupla:
    print('número 3 na posição',tupla.index(3)+1, end=' ')
else:
    print('não tem numeros 3')
print('\n','o 9 apareceu', tot9, 'vezes')
print('no total tem', totpar, 'numeros pares')
