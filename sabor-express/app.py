import os

restaurantes = [{'nome':'JapaIn', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Sumprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_do_programa():
    '''Esta função exibe o nome do programa em caracteres especiais'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    '''Esta função exibe as quatro opções principais do app'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    '''Esta função encerra o app'''
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Esta função informa que a opção escolhida é inválida'''
    print ('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Esta imprime na tela o título da opção escolhida pelo usuário'''
    os.system('cls')
    linha ='*' * (len(texto)+4)
    print (linha)
    print(f'* {texto} *')
    print (linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
       
        Inputs: 
        - Nome do Restaurante
        - Categoria do restaurante

        Outputs:
        - adicionar um novo restaurante na lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    #restaurantes.append(nome_do_restaurante)
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Esta função lista, de forma tabular, os restaurantes cadastrados
    
        outputs:
        nome, categoria e status de todos os restaurantes cadastrados'''
    
    exibir_subtitulo('Listando os restaurantes cadastrados')
    # print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    nome_restaurante = 'Nome do restaurante'
    categoria = 'categoria'  
    print(f'{nome_restaurante.ljust(22)} | {categoria.ljust(20)} | Status')


    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''Esta função altera o estado do restaurante ativo/inativo
        input:
        - nome do restaurante
        
        output
        - troca do valor ativo do restaurante escolhido'''
    
    exibir_subtitulo('Alterar estado do restaurante')
    nome_restaurante = input('Insira o nome do restaurante que deseja altarar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem =f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado cmo sucesso'
            print(mensagem)
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''Esta função executa a rotina referente a opção escolhida pelo usuário
        Input:
        - opção escolhida pelo usuário
        
        output:
        - executar as funções
            cadastrar_novo_restaurante()
            listar_restaurantes()
            alternar_estado_restaurante()
            finalizar_app()
            opcao_invalida()'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()