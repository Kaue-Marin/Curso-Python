aluno = {}
aluno['nome'] = str(input('nome: '))
aluno['média'] = float(input('média: '))
print(f'nome é igual a {aluno["nome"]}')
print(f'média é igual a {aluno["média"]}')
if aluno['média'] > 5:
    print('aprovado')
elif (aluno['média'] > 5 ) and (aluno['média'] <= 6.5):
        print('recuperação')
elif aluno['média'] < 5:
    print('reprovado')