lista = []
while True:
    lista.append(int(input('digite um valor: ')))
    c = input('quer continuar? [s/n]: ')
    if c == 'n':
        break
dec = sorted(lista, key = int,reverse=True)
if 5 in lista:
    print('o 5 está na lista')
else:
    print('o 5 não está na lista')
print(f'ao todos tivemos {len(lista)} valores digitados')
print('a lista em ordem decrescente é', dec)
