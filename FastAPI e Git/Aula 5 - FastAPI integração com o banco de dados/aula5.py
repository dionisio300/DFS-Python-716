'''
DROP DATABASE IF EXISTS loja_api; 
CREATE DATABASE loja_api; 
USE loja_api; 
 
CREATE TABLE usuarios ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL UNIQUE 
); 
 
CREATE TABLE produtos ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(100) NOT NULL, 
    preco DECIMAL(10, 2) NOT NULL 
); 
 
CREATE TABLE pedidos ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    usuario_id INT NOT NULL, 
    produto_id INT NOT NULL, 
    quantidade INT NOT NULL, 
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id), 
    FOREIGN KEY (produto_id) REFERENCES produtos(id) 
); 
 -- Dados de exemplo 
INSERT INTO usuarios (nome, email) VALUES 
('Alice', 'alice@email.com'), 
('Bruno', 'bruno@email.com'), 
('Carla', 'carla@email.com'); 
 
INSERT INTO produtos (nome, preco) VALUES 
('Teclado', 199.90), 
('Mouse', 99.90), 
('Monitor', 1299.00); 
 
INSERT INTO pedidos (usuario_id, produto_id, quantidade) VALUES 
(1, 1, 2), 
(2, 3, 1), 
(3, 2, 3);






Comando do terminal
=====================================================
pip install fastapi uvicorn mysql-connector-python

.\.venv\Scripts\activate





Faça uma API 
GET /usuarios -> listar todos os usuários
GET /produtos -> Listar todos os produtos
GET /pedidos -> Listar todos os pedidos
GET /usuarios/1/pedido -> Listar pedidos do usuário 1
GET /usuarios/1/resumo-compras -> retornar o total gasto e quantidade de itens comprados pelo usuário 1







Faça uma API 
GET /usuarios -> listar todos os usuários
GET /produtos -> Listar todos os produtos
GET /pedidos -> Listar todos os pedidos
GET /usuarios/1/pedido -> Listar pedidos do usuário 1
GET /usuarios/1/resumo-compras -> retornar o total gasto e quantidade de itens comprados pelo usuário 1

'''
from fastapi import FastAPI
import mysql.connector as my

app = FastAPI()

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



@app.get("/usuarios")
def usuarios():
    return listarUsuarios()

def listarPedidosUsuarios(id_usuario):
    #estabecer a conexão
    conexao = conectar_banco()
    #criar o cursor
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from pedidos where usuario_id = 1;'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado




@app.get('/usuarios/{id_usuario}/pedido')
def pedidosUsuarios(id_usuario:int):

    return listarPedidosUsuarios(id_usuario)



'''
Versão final

=============================================================


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