def fatorial(numero, show=False):
    """
    -> calcula o fatorial de um número.
    :param n: o numero a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    return: o valor de um fatorial de um numero n.


    """
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(f' {c}', end=' ')
        if c > 1:
            print(' x ', end=' ') 
        else:
            print(' = ', end=' ') 
        f *= c
    return f
# programa principal
n = int(input('digite um numero: '))
print(fatorial(n, show=True))
help(fatorial)