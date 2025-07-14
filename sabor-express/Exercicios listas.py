#Exercício 1 e 2
# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Ricardo', 'Angelita']
ano = [1971, 2025]

for numero in numeros:
    print(f' a lista de números é {numero}')

print()
for nome in nomes:
    print(f'nome: {nome}')

print()
for ano_i in ano:
    print(f'Ano: {ano_i}')

#Exercício 3
#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

contador = 0
for x in range(10):
    if x%2 == 1:
        contador = contador+x
print(contador)

#Exercício 4
# # 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for x in range(10, 0,-1):
    print(x, end=' - ')

#Exercício 5
# # 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Selecione o multiplicador da taboada: '))
print(f'\nTABOADA DE [numero]:\n')
for x in range(11):
    multiplicacao = x*numero
    print(f'{numero} x {x} = {multiplicacao}')


#Exercício 6
# # 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.

numeros = [1,2,3,4,"78",6,7,8,9,10]
soma=0
try:
    for numero in numeros:
        soma = soma+numero
        print(soma)
except TypeError:
    print ('uma das entradas não é um número válido')

#Exercício 7
# # 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco
#  try-except para lidar com a divisão por zero, caso a lista esteja vazia.

# numeros = [] #lista zerada
# numeros = [1,2,3,4,'5'] #lista com tipo errado
numeros = [1,2,3,4,5] 

soma=0
elemento = len(numeros)
print('#      Soma  -  Média')
try:
    for numero in numeros:
        soma = soma+numero
    print(f'{elemento}.        {soma}      {soma/elemento}')

except TypeError:
    print ('Erro:tipo')
except ValueError:
    print ('Erro:valor')
except ZeroDivisionError:
    print ('Erro: DIvisão por zero')
finally:
    print(f'- Fim -')

