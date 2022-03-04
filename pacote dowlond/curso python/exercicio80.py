lista = []
for n in range(0,5):
    v = int(input(f'digite o {n} valor: '))
    if n == 0 or n > max(lista):
        lista.append(v)
    else:
        for p,c in enumerate(lista):
            if v <= c:
                lista.insert(p, v)
                break
print(lista)

