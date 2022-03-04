def ficha(jog='desconhecido', gols=0):
    print(f'o jogador {jog} fez {gols} gols ')


# programa principal
n = str(input('nome do jogador: '))
g = str(input('gols do jogador: '))
if g.isnumeric():
    g = int(g)
else:
    g = '0'
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)