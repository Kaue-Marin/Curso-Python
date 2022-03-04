jogador = {}
gp = []
totgols = 0
jogador['nome'] = str(input('nome do jogador: '))
jogador["partidas"] = int(input('partidas jogadas: '))
for p in range (jogador["partidas"]):
    gp.append(int(input(f'quantos gols fez na partida: {p}: ')))
total = sum(gp)
print(jogador)
print(f'o campo nome tem o valor {jogador["nome"]}')
print(f'o campo gols tem o valor {gp}')
print(f'o campo total tem o valor {total}')
for k, v in enumerate(gp): 
    print(f' na partida {k} fez {v} gols')
     