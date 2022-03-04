lista = []
listaimpar = []
listapar = []
while True:
    v = int(input('digite um valor: '))
    lista.append(v)
    c = input('quer continuar? [s/n]: ')
    if v%2==0:
        listapar.append(v)
    else:
        listaimpar.append(v)
    if c == 'n':
        break
print('TODA LISTA: ', lista)
print('PARES: ', listapar)
print('IMPARES: ', listaimpar)