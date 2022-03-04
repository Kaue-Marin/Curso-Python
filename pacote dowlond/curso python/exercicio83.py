lista = []
pilha = []
exp = str(input('digite a expressão: '))
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('sua expressão está valida')
else:
    print('sua expressão não está valida')