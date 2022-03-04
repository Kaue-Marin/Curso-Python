palavra = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavra :
    print(f'\n na palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')