# import mysql.connector as ms

# config = { 
#   'user': 'root', 
#   'password': '1234', 
#   'host': 'localhost', 
#   'database': 'loja', 
# }
# # Estabelecendo a conexão 
# conexao = ms.connect(**config) 
 
# # Criando um cursor para executar queries 
# cursor = conexao.cursor(dictionary=True) 

# # sql = 'select * from produtos'
# # cursor.execute(sql)
# # resposta = cursor.fetchall()

# def listar_produtos():
#     sql = 'select * from produtos'
#     cursor.execute(sql)           
#     resposta = cursor.fetchall() # resposta = [{nome,preco,quantidade},{},{},...]
#     for resp in resposta:
#         print(f'Nome: {resp['nome']}, Preço: {resp['preco']}, QTD: {resp['quantidade']}, ID: {resp['id']}')
#     return resposta

# def atualizarQuantidade(id,quantidade):
#     sql = 'update produtos set quantidade = %s where id = %s'
#     valores = (quantidade,id)
#     cursor.execute(sql,valores)
#     conexao.commit()
    
#     print('Atualização realizada com sucesso!')

# def buscarProduto(nome):
#     sql = 'select * from produtos where nome = %s'
#     valores = (nome,)
#     cursor.execute(sql,valores)
#     resposta = cursor.fetchall()
#     for resp in resposta:
#         print(f'Id: {resp['id']}, Nome: {resp['nome']}, Preço: {resp['preco']}, Quantidade: {resp['quantidade']}')




# class Produto:
#     def __init__(self,nome,preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade
#     def salvar_no_banco(self):
#         sql = 'insert into produtos (nome, preco, quantidade) values (%s,%s,%s)'
#         valores = (self.nome,self.preco,self.quantidade)
#         cursor.execute(sql,valores)
#         conexao.commit()
        
#         print('Produto Adicionado com sucesso!')

# while True:
#     opcao = input('1 - Cadastrar Produto\n2 - Listar\n3 - Atualizar Quantidade\n4 - Buscar\n5 - Sair\n')
#     if opcao == '5':
#         print('Saindo...')
#         break
#     if opcao == '1':
#         nome = input('Nome: ')
#         preco = float(input('Preço: '))
#         quantidade = int(input('Quantidade: '))

#         produto = Produto(nome,preco,quantidade)
#         produto.salvar_no_banco()
#     if opcao == '2':
#         listar_produtos()
#     if opcao == '3':
#         id = int(input('ID: '))
#         novaQuantidade = int(input('Quantidade: '))
#         atualizarQuantidade(id,novaQuantidade)
#     if opcao == '4':
#         nome = input('Nome: ')
#         buscarProduto(nome)


from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def read_root():
    return {"mensagem":"Olá mundo!"}