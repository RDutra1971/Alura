# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome':'Ricardo', 'idade':53, 'cidade':'Petropolis'}
          
# 2 - Utilizando o dicionário criado no item 1:
#         Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#         Adicione um campo de profissão para essa pessoa;
#         Remova um item do dicionário.
print(pessoa)
pessoa['nome']= 'Paulo'
pessoa['idade']= 26
del pessoa['cidade']
pessoa['profissao'] = 'Engenheiro'

print(pessoa)
print()


# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.
lista_num={}
for numero in range(1,6,1):
    lista_num[str(numero)]=numero*numero
print(lista_num)   

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
pessoa = {'nome':'Ricardo', 'idade':53, 'cidade':'Petropolis'}

if 'verbo' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
frase = 'eu tu ele nos vos eles eu tu ele nos vos eles eu tu ele nos vos eles aviao carro carneiro barco'
contagem_de_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_de_palavras[palavra] = contagem_de_palavras.get(palavra, 0) + 1
print(contagem_de_palavras)

