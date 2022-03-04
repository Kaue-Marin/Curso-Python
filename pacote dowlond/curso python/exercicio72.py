# 1. ler valor entre 0 e 20
c = 's'
while c == 's':
    valor = int(input('digite um valor entre 0 e 20: '))
    while (valor > 20) or (valor < 0):
        valor = int(input('digite um valor entre 0 e 20: '))
# 2. valor e igual a numero por extenso
    ex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove,', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete','dezoito','dezenove','vinte' )
# 3. se valor for menor que 0 e maior que vinte repetir
    print(ex[valor])
    c = input('você quer continuar? [s/n]: ')
# 4. mostrar numero por extenso