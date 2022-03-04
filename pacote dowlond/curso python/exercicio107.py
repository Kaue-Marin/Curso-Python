import utilidadesCeV.moeda as moeda

p = float(input('digite o preço: R$'))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'aumentamos 10% de {p} temos {moeda.aumentar(p, 10)}')
print(f'diminuindo 13% de {p} temos {moeda.diminuir(p, 13)}')