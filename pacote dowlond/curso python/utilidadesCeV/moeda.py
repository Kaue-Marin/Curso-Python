def aumentar(preco=0,taxa=0,format=False):
    aum =  (preco * taxa )/100
    res = preco + aum
    return res if format is False else moeda(res)

def diminuir(preco=0,taxa=0,f=False):
    aum =  (preco * taxa )/100
    res = preco - aum
    return res if format is False else moeda(res)

def dobro(preço=0, format=False):
    res = preço * 2
    return res if format==False else moeda(res)

def metade(preço=0, format=False):
    res = preço / 2
    return res if format==False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',') 

def resumo(preco=0, aum=5, red=10):
    print(f'preço analisado: {preco}')
    print(f'dobro do preço: {dobro(preco, True)}')
    print(f'metade do preço: {metade(preco, True)}')
    print(f'{aum}% de aumento: {aumentar(preco, 10, True)}')
    print(f'{red}% de redução: {diminuir(preco,10, True)}')