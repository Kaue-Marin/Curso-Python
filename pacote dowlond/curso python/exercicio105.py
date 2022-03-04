def notas(*num, sit = False):
    """
    -> Funçao para analisar notas e situaçao de vários alunos
    :param nota: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situaçao
    :return: dicionário com várias informaçoes sobre a situaçao da turma.
    """

    r = dict()
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] > 7 :
            r['situação'] = 'boa'
        elif r['media'] < 7 and r['media'] > 4.9:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r
# programa principal
resp = notas(3,5,2, sit=True)
print(resp)
help(notas)