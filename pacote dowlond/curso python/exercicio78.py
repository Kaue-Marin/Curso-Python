valores = list()
maior = 0
menor = 999
for cont in range(0,5):
    valores.append(int(input(f'digite um valor na posição {cont}: ')))
    if cont == 0:
       maior = menor = valores[cont]
    else:
       if valores[cont] > maior:
          maior = valores[cont]
       if valores[cont] < menor:
          menor = valores[cont]
print(f'o maior valor digitado foi {maior} na posição {valores.index(maior)}')
print(f'o menor valor digitado foi {menor} na posição {valores.index(menor)}')