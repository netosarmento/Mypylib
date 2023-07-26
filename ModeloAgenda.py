AGENDA = {}

def mostrar_contato():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('Agenda vazia')

def buscar_contato(contato):
    try:
        print('Nome:', contato)
        print('email:', AGENDA[contato]['email'])
        print('telefone:', AGENDA[contato]['telefone'])
        print('endereco:', AGENDA[contato]['endereco'])
    except KeyError:
        print('-->> Contato Inexistente')

def ler_detalhes():
    telefone = input('Telefone do contato: ')
    email = input('email do contato: ')
    endereco = input('Endereço do contato: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco
    }
    salvar()
    print('----> Contato {} adicionado/editado com sucesso'.format(contato))

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print('---> Contato {} excluído com sucesso'.format(contato))
    except KeyError:
        print('-->> Contato Inexistente')

def exportar_contato(nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for contato, detalhes in AGENDA.items():
                telefone = detalhes['telefone']
                email = detalhes['email']
                endereco = detalhes['endereco']
                arquivo.write('{}; {}; {}; {}\n'.format(contato, telefone, email, endereco))
        print('Agenda exportada com Sucesso')
    except Exception as error:
        print('Algum erro ocorreu ao exportar contatos')
        print(error)

def importar_contatos(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split('; ')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
        print('Contatos importados com sucesso!')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except Exception as error:
        print('Algum erro ocorreu')
        print(error)

def salvar():
    exportar_contato('database.csv')

def carregar():
    importar_contatos('database.csv')
    
def imprimir_menu():
    print('1- Mostrar todos os contatos')
    print('2- Buscar contato')
    print('3- Incluir contato')
    print('4- Editar contato')
    print('5- Excluir contato')
    print('6- Exportar para arquivo CSV')
    print('7- Importar arquivo CSV')
    print('0- Fechar Programa')

carregar()
while True:
    imprimir_menu()

    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        mostrar_contato()
    elif opcao == '2':
        contato = input('Nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('Nome do contato: ')
        if contato in AGENDA:
            print('Contato já existente:', contato)
        else:
            telefone, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Nome do contato: ')
        if contato in AGENDA:
            print('Editando Contato:', contato)
            telefone, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, telefone, email, endereco)
        else:
            print('- Contato Inexistente')
    elif opcao == '5':
        contato = input('Nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contato(nome_arquivo)
    elif opcao == '7':
        nome_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_arquivo)
    elif opcao == '0':
        print('Fechando programa')
        break
    else:
        print('Opção inválida')
