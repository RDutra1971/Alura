print('Python na Escola de Programação da Alura\n')

nome='Ricardo'
idade=53

print(f'Meu nome é {nome} e tenho {idade} anos.\n ')

print("""
    A
    L
    U
    R
    A""")

pi = 3.14159

# Abordagem de f-string
print(f'1 - O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('2 - O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('3 - O valor arredondado de pi é:', round(pi, 2))