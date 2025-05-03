import mysql.connector as my

def conectar_banco():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'loja'
    )
    return conexao


def buscar_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary = True)
    sql = 'select * from clientes'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    print(resultado)

    conexao.close()
    return resultado

def inserir_clientes(nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'insert into clientes(nome) values (%s)'
    cursor.execute(sql,(nome,))
    conexao.commit()
    print('O cliente foi inserido no banco de dados!')
    conexao.close()

def atualizar_preco(novoPreco, id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'update produtos set preco = %s where id = %s'
    cursor.execute(sql,(novoPreco,id))
    conexao.commit()
    print('Preço atualizado com sucesso!!')
    conexao.close()

def deletar_cliente(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'delete from clientes where id = %s'
    cursor.execute(sql,(id,))
    conexao.commit()
    print('Cliente deletado com sucesso!!')
    conexao.close()


while True:
    opcao = input('1 - Listar Clientes\n2 - Inserir Clientes\n3 - Atualizar o Preço\n4 - Deletar Cliente\n5 - Sair\n')
    if opcao == '5':
        print('Saindo...')
        break
    if opcao == '1':
        buscar_clientes()
    if opcao == '2':
        nome = input('Nome do clinete: ')
        inserir_clientes(nome)
    if opcao == '3':
        id = input('ID do produto: ')
        novoPreco = input('Digite o novo preço: ')
        atualizar_preco(novoPreco, id)
    if opcao == '4':
        id = input('ID do cliente: ')
        deletar_cliente(id)
