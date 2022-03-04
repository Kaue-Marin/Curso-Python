def voto(ano):
    nasc = 2022 - ano
    if nasc < 18:
        return f'você tem {nasc} anos. voto negado'
    elif nasc >= 18 and nasc < 65:
        return f'você tem {nasc} anos. voto obrigatório'
    else:
        return f'você tem {nasc} anos. voto opcional'
# programa principal
ano = int(input('em que ano você nasceu: '))
print(voto(ano))