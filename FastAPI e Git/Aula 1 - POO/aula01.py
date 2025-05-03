import mysql.connector as my

def conectar_banco():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'escola'
    )
    return conexao
'''
SELECT
Conectar com o banco
criar o cursor
fazer o sql
executar o sql
trazer os resultados
fechar a conexão
retornar os resultados
'''
def consultar_alunos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from alunos'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

'''
INSERT, UPDATE, DELETE
Conectar com o banco
criar o cursor
fazer o sql
executar o sql
commit
fechar a conexão
retornar uma mensagem
'''

def inserir_aluno(nome,matricula):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'insert into alunos(nome, matricula) values (%s, %s)'
    cursor.execute(sql,(nome,matricula))
    conexao.commit()
    conexao.close()
    return 'Dados inseridos com sucesso'


def atualizar_nome(id, nome):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'update alunos set nome = %s where id_aluno = %s'
    cursor.execute(sql,(nome,id))
    conexao.commit()
    conexao.close()
    return 'Nome atualizado com sucesso!!'

def deletar_aluno(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    sql = 'delete from alunos where id_aluno = %s'
    cursor.execute(sql,(id,))
    conexao.commit()
    conexao.close()
    return 'Aluno deletado com sucesso!!'



opcoes = input('1 - Consultar a lista de alunos\n2 - Inserir novo aluno\n3 - Atualizar nome do aluno\n4 - Deletar aluno\n5 - Sair')
while True:
    if(opcoes == '5'):
        print('Saindo...')
        break
    if(opcoes == '1'):
        alunos = consultar_alunos()

        for aluno in alunos:
            print(f'ID: {aluno['id_aluno']} - Nome: {aluno['nome']} - Matrícula = {aluno['matricula']}')
    if(opcoes == '2'):
        nome = input('Nome: ')
        matricula = input('Matricula: ')
        print(inserir_aluno(nome,matricula))
    
    if(opcoes == '3'):
        id = input('ID: ')
        nome = input('Nome: ')
        print(atualizar_nome(id,nome))
    if(opcoes == '4'):
        id = input('ID: ')
        print(deletar_aluno(id))


    opcoes = input('1 - Consultar a lista de alunos\n2 - Inserir novo aluno\n3 - Atualizar nome do aluno\n4 - Deletar aluno\n5 - Sair')


'''
ls - Lista as pastas e arquivos dentro de um diretório
cd 'nome da pasta'-> Muda de pasta
cd .. -> voltar um nível no terminal
'''




