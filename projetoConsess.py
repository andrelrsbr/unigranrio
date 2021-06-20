'''
• efetuar o CRUD de Clientes
• efetuar o CRUD de Motocicletas
• efetuar a venda de Motocicletas
• fornecer listagem de Vendas
• permitir a consulta de uma venda específica, incluindo o cliente e motocicleta
relacionada a mesma'''


def pularLinha():
    print('')


def mostraLinha():
    print('-' * 40)


def titulo(msg):
    mostraLinha()
    print(msg.center(40))
    mostraLinha()


def exibirMenu():
    pularLinha()
    print('1. Cadastrar cliente\n2. Alterar cliente\n3. Listar clientes\n4. Apagar clientes\n5. Cadastrar veículo\n6. Listar veículos\n7. Sair ')
    pularLinha()


def cadastrarClientes(clientes):

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('CADASTRO DE CLIENTES:')
    identif = int(input('Informe o CPF: '))
    nome = input('Nome completo: ')
    email = input('Email: ')
    #clientes.append((identif, nome, idade))
    #print('Cadastrado realizado com sucesso!')
    #pularLinha()

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO Clientes (CPF, nome, email)
    VALUES (?,?,?)
    """, (identif, nome, email))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()


def listarClientes(clientes):
    pularLinha()
    titulo('LISTA DE CLIENTES CADASTRADOS:')
    #for cliente in clientes: #PARA CADA CLIENTE NA LISTA CLIENTES
    #    identif, nome, idade = cliente
    #    print(f'Nome:{nome} | Idade: {idade} | Id: {identif}')

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
    SELECT * FROM Clientes;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    pularLinha()

def alterarClientes(clientes):
    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('ALTERAR CLIENTE')
    cpf = int(input('Informe o CPF do cliente: '))
    nome_alt = input('Informe o novo nome: ')
    email_alt = input('Informe o novo email: ')

    #id_cliente = 1
    #novo_fone = '11-1000-2014'
    #novo_criado_em = '2014-06-11'

    # alterando os dados da tabela
    cursor.execute("""
    UPDATE Clientes
    SET Nome = ?, Email = ?
    WHERE CPF = ?
    """, (nome_alt, email_alt, cpf))

    conn.commit()

    print('Dados atualizados com sucesso.')

    conn.close()


    pularLinha()


'''
def buscarClientes(clientes):
    pularLinha()
    titulo('BUSCAR CLIENTE')
    identif_desejado = int(input('Informe o Id do cliente: '))
    for cliente in clientes:
        identif, nome, idade = cliente
        if identif == identif_desejado:
            pularLinha()
            titulo('RESULTADO DA CONSULTA:')
            print(f'Nome: {nome}\nIdade: {idade}\nId: {identif}')
            break
    else:
        print(f'Pessoa com ID {identif_desejado} nao encontrada.')
    pularLinha()

'''

def apagarClientes(clientes):
    pularLinha()

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    titulo('APAGAR CLIENTE')
    cpf = int(input('Informe o CPF do cliente: '))

    # excluindo um registro da tabela
    cursor.execute("""
    DELETE FROM Clientes
    WHERE cpf = ?
    """, (cpf,))

    conn.commit()

    print('Registro excluido com sucesso.')

    conn.close()

    '''
    for cliente in clientes:
        identif, nome, idade = cliente
        if identif == identif_desejado:
            pularLinha()
            titulo('RESULTADO DA CONSULTA:')
            print(f'Nome: {nome}\nIdade: {idade}\nId: {identif}')
            break
    else:
        print(f'Pessoa com ID {identif_desejado} nao encontrada.')
    pularLinha()
    
    '''

def cadastrarMotos(motos):
    pularLinha()
    titulo('CADASTRO DE MOTOCICLETA:')
    identifMoto = int(input('Id: '))
    marca = input('Marca: ')
    modelo = (input('Modelo: '))
    motos.append((identifMoto, marca, modelo))
    print('Cadastrado realizado com sucesso!')
    pularLinha()


def listarMotos(motos):
    pularLinha()
    titulo('LISTA DE MOTOCICLETAS CADASTRADAS:')
    for moto in motos:
        identif, marca, modelo = moto
        print(f'Id: {identif} | Marca: {marca} | Modelo: {modelo}')
    pularLinha()


def iniciarPrograma():
    clientes = []
    motos = []
    while True:
        exibirMenu()
        opcao = int(input('Escolha a opçao: '))
        if opcao == 1:
            cadastrarClientes(clientes)
        elif opcao == 2:
            alterarClientes(clientes)
        elif opcao == 3:
            listarClientes(clientes)
        elif opcao == 4:
            apagarClientes(clientes)
        elif opcao == 5:
            cadastrarMotos(motos)
        elif opcao == 6:
            listarMotos(motos)
        elif opcao == 7:
            print('Programa finalizado!')
            break
        else:
            print('Opção inválida. Tente novamente.')


# Fazer sistema de vendas
# Fazer uma validaçao da entrada de 'opçao'
# Fazer um 'voltar para menu' ou 'finalizar programa' para nao ficar retornando sempre o menu de opçoes completo.


#INÍCIO DO PROGRAMA

titulo('SISTEMA CONCESSIONÁRIA')
iniciarPrograma()





