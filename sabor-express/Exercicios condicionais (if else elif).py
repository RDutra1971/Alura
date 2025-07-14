# Exercício 1
numero= int(input('Escolha um número: '))
resto  = numero % 2
if resto == 0: 
   print(f'O número {numero} é par\n')
else: print(f'O número {numero} é impar\n')


# Exercício 2
# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else 
# para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade= int(input('Inorme sua idade: '))
if 0<= idade <=12: 
    print(f'A idade de {idade} é de uma criança\n')
elif 13<= idade <=18: 
    print(f'A idade de {idade} é de um adolescente\n')
else:
    print(f'A idade de {idade} é de um adulto\n')

# Exercício 3
# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para
# verificar se o nome de usuário e a senha fornecidos correspondem aos valores 
# esperados determinados por você.

nome_cadastro = "Ricardo"
senha_cadastro = "R!c@rd0"
nome = input('Usuário :')
senha = input ('Senha :')

if (nome == nome_cadastro) and (senha == senha_cadastro):
    print (f'Usuário {nome} já cadastrados!\n')
else:
    print (f'Usuário {nome} não cadastrado\n')

# Exercício 4
# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para
# determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:
# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

coord_x = int(input('Coordenada X: '))
coord_y = int(input('Coordenada y: '))
if coord_x > 0 and coord_y >0: 
     print(f'A coordenada ({coord_x}, {coord_y}) pertence ao primeiro quadrante\n')
elif coord_x < 0 and coord_y >0: 
     print(f'A coordenada ({coord_x}, {coord_y}) pertence ao segundo quadrante\n')
elif coord_x < 0 and coord_y <0: 
     print(f'A coordenada ({coord_x}, {coord_y}) pertence ao terceiro quadrante\n')
elif coord_x > 0 and coord_y <0: 
     print(f'A coordenada ({coord_x}, {coord_y}) pertence ao quarto quadrante\n')
else:
     print(f'A coordenada ({coord_x}, {coord_y}) pertence a origem\n') 

# coord_x = int(input('Coordenada X: '))
# coord_y = int(input('Coordenada y: '))

# match {coord_x, coord_y}:
#     case  coord_x>0 and coord_y>0: 
#         print(f'A coordenada ({coord_x}, {coord_y}) pertence ao primeiro quadrante\n')
#     case  <0, >0: 
#         print(f'A coordenada ({coord_x}, {coord_y}) pertence ao segundo quadrante\n')
#     case  <0, <0: 
#         print(f'A coordenada ({coord_x}, {coord_y}) pertence ao terceiro quadrante\n')
#     case  >0, <0: 
#         print(f'A coordenada ({coord_x}, {coord_y}) pertence ao quarto quadrante\n')
#     case  = 0, = 0: 
#         print(f'A coordenada ({coord_x}, {coord_y}) pertence a origem\n') 

