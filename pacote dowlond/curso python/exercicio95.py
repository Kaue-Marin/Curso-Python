jogador = {}
gp = []
time = []
while True:
    jogador.clear()
    totgols = 0
    jogador['nome'] = str(input('nome do jogador: '))
    jogador["partidas"] = int(input('partidas jogadas: '))
    gp.clear()
    for p in range (jogador["partidas"]):
        gp.append(int(input(f'quantos gols fez na partida: {p}: ')))
        total = sum(gp)
    time.append(jogador.copy())
    print(jogador)
    print(f'o campo nome tem o valor {jogador["nome"]}')
    print(f'o campo gols tem o valor {gp}')
    print(f'o campo total tem o valor {total}')
    for k, v in enumerate(gp): 
        print(f' na partida {k} fez {v} gols')
    c = str(input('quer continuar [s/n]: '))
    if c == 'n':
        break
for k, v in enumerate(time):
    print(f'{k}', end=' ')
for d in v.values():
    print(d, end=' ')
print()
while True:
    opc = int(input('mostrar medias de qual jogador? (interrompe 999): '))
    if opc == 999:
        break
    if opc > len(jogador):
        break
    else:
        print(f'o jogador {time[opc]["nome"]}' )
        for i,g in enumerate (gp):
            print(f'no jogo {i+1} fez {g} gols')