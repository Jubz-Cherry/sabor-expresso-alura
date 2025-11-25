import os

restaurantes = [
    { 'nome': 'Os Comilões', 'categoria': 'Hamburgueria', 'ativo': False },
    { 'nome': 'Pizzaria do Zé', 'categoria': 'Pizza', 'ativo': True },
    { 'nome': 'Com Sabor de Casa', 'categoria': 'Comida Caseira', 'ativo': False }
]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    ''' Essa função é responsavel por mostrar as opções do menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função é responsavel por finalizar a aplicação''' 
    exibir_subtitulo('Finalizando aplicação... Até mais!')

def voltar_ao_menu_principal():
    ''' Essa função é responsavel por voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal...')
    main()

def opcao_invalida():
    ''' Essa função é responsavel por tratar opções inválidas'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    ''' Essa função é responsavel por colocar um subtitulo na tela'''
    os.system('cls')
    linha = '*' * (len(texto)) 
    print(linha)
    print(texto) 
    print(linha)  
    print()

def cadastrar_novo_restaurante():
    ''' Essa função é responsavel por cadastrar novos restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria
    - Status (ativo ou inativo)

    Outputs
    - Adiciona o novo restaurante na lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    ''' Essa função é responsavel por listar os restaurantes'''
    exibir_subtitulo('Lista de restaurantes cadastrados: ')

    print(f'{'Nome do restaurante'.ljust(20)} | {"Categoria".ljust(20)} | {"Status"}\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')
    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    ''' Essa função é responsavel por alterar o estado do restaurante'''
    exibir_subtitulo('Alterando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
   
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True 
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')

    voltar_ao_menu_principal()



def escolher_opcoes():
    ''' Essa função é responsavel por escolher as opções do menu principal'''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante() 

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()

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
    escolher_opcoes()



if __name__ == '__main__': 
    main()