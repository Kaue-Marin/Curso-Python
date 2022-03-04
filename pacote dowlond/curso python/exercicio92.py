dados = dict()
dados['nome'] =  str(input('nome: '))
dados['nasc'] =  int(input('ano de nascimento: '))
dados['idade'] = 2022 - dados['nasc']
dados['ctps'] =  int(input('carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['ano'] = int(input('ano de contratação: '))
    dados['salário'] =  float(input('sálario: '))
    dados['aposentadoria'] = (dados['ano'] + 35) - 2022
    print(f'faltam {dados["aposentadoria"]} anos para você se aposentar')
