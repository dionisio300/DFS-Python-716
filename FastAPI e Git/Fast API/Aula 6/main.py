'''
Faça uma API 
GET /usuarios -> listar todos os usuários
GET /produtos -> Listar todos os produtos
GET /pedidos -> Listar todos os pedidos
GET /usuarios/1/pedido -> Listar pedidos do usuário 1
GET /usuarios/1/resumo-compras -> retornar o total gasto e quantidade de itens comprados pelo usuário 1

'''
from fastapi import FastAPI
import mysql.connector as my
from pydantic import BaseModel

app = FastAPI()

class UsuarioInput(BaseModel):
    nome:str
    email:str


def conectar_banco():
    config = { 
    'user': 'root', 
    'password': '1234', 
    'host': 'localhost', 
    'database': 'loja_api', 
    }
    conexao = my.connect(**config)
    return conexao


def listarUsuarios():
    #estabecer a conexão
    conexao = conectar_banco()

    #criar o cursor
    cursor = conexao.cursor(dictionary=True)

    #Query a ser executada
    sql = 'select * from usuarios'

    #Executar a Query
    cursor.execute(sql)

    #Passa os resultados da Query para a variável resultado
    resultados = cursor.fetchall()

    #fechar a conexão
    conexao.close()

    return resultados



@app.post('/usuarios')
def criar_usuario(usuario:UsuarioInput):
    #estabecer a conexão
    conexao = conectar_banco()

    cursor = conexao.cursor(dictionary=True)

    sql = 'insert into usuarios (nome,email) values (%s,%s)'

    cursor.execute(sql,(usuario.nome,usuario.email))

    conexao.commit()
    conexao.close()

    return {'mensagem':'Usuario criado com sucesso!!'}



@app.get("/usuarios")
def usuarios():
    return listarUsuarios()

def listarPedidosUsuarios(id_usuario):
    #estabecer a conexão
    conexao = conectar_banco()
    #criar o cursor
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from pedidos where usuario_id = 1;'
    cursor.execute()
    resultado = cursor.fetchall()
    return resultado


@app.get('/usuarios/{id_usuario}/pedido')
def pedidosUsuarios(id_usuario:int):

    return listarPedidosUsuarios(id_usuario)