def maior(*num):
    c =  maior = 0
    for n in num:
        print(n, end=' ')
        if c == 0:
            maior = n
        else:
            if n > maior:
                maior = n 
        c += 1

    print(f'foram informados ao todo {c} numeros ')
    print(f'o maior valor informado foi {maior}')
# programa princicpal
maior(1,2,3,4,5,6)

