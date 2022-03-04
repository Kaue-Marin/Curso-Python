valores = []
while True:
    v = int(input('digite os valores: '))
    c = input('quer continuar? [s/n]: ')
    if c == 'n':
        break
    if v not in valores:
        valores.append(v)
        print('numero adicionado com sucesso...')
    else:
        print('numero duplicado, não irei adicionar...')
valores.sort()
print('—' * 40)
print(f'A lista em ordem crescente é {valores}')