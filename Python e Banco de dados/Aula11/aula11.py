import mysql.connector as my

def conectar_banco():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'loja'
    )
    return conexao

# select
def ler_tabela_clientes():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    nome = input('Nome: ')
    sql = 'select * from clientes where nome = %s'
    cursor.execute(sql,(nome,))
    resultados = cursor.fetchall()
    conexao.close()
    print(resultados)


def inserir_produtos(nome, preco):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'insert into produtos (nome, preco) values (%s, %s)'
    cursor.execute(sql,(nome,preco))
    conexao.commit()
    conexao.close()
    print('Dados inseridos com sucesso!!')


nomeProduto = input('Nome: ')
preco = input('Preço: ')
inserir_produtos(nomeProduto,preco)