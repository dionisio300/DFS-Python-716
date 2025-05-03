'''
Banco de dados

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
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) on delete cascade, 
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
(1, 3, 1), 
(1, 2, 3);

select * from usuarios;

select * from produtos;

select * from pedidos;

select * from pedidos where usuario_id = 1;

/*Create*/
insert into usuarios (nome, email) values 
('Maria','maria@gmail.com'),
('Ana','ana@gmail.com');

/*Read*/
select * from usuarios;
select * from pedidos;

/*Update*/
update usuarios set nome = 'Bruno' where id = 1;

/*Delete*/


Arquivos iniciais
========================================================
Projeto
| - main.py (Código do python)
| - .gitignore (.venv)
| - readme.md (Explicação do projeto)
| - requirements.txt -> bibliotecas (fastapi uvicorn mysql-connector-python)




Comandos terminal
=======================================================


pip install fastapi uvicorn mysql-connector-python (instalar as bibliotecas)
python -m venv .venv (configurar servidor local)
.\.venv\Scripts\activate (Ativar scripts do servidor local)
uvicron main:app --reload (iniciar o servidor)
ctrl + c (parar o servidor)




main.py
===================================================================
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

@app.get("/")
def paginaInicial():
    return {"msg":"olá mundo"}




#==============================================================================
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

@app.get("/")
def paginaInicial():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from usuarios'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    return resultado

#=========================================================================
'''
Crie uma API utilizando FastAPI e MySQL que simule uma loja com o seguinte cenário:

A loja possui clientes e alunos (que são participantes de cursos oferecidos pela loja). Você deve:

Criar o banco de dados e as tabelas necessárias no MySQL.

Criar rotas para realizar todas as operações CRUD para:

Clientes

Alunos

As rotas devem permitir:

Listar todos os registros (GET)

Obter um registro por ID (GET)

Inserir um novo registro (POST)

Atualizar o curso do aluno ou o e-mail do cliente um registro existente (PUT)

Deletar um registro (DELETE)



======================================================================

-- Criação do banco de dados
CREATE DATABASE loja_api;

-- Seleciona o banco
USE loja_api;

-- Tabela clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Tabela alunos
CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    curso VARCHAR(100) NOT NULL
);

INSERT INTO clientes (nome, email) VALUES
('Ana Souza', 'ana.souza@email.com'),
('Bruno Lima', 'bruno.lima@email.com'),
('Carla Mendes', 'carla.mendes@email.com'),
('Diego Rocha', 'diego.rocha@email.com'),
('Eduarda Silva', 'eduarda.silva@email.com'),
('Felipe Alves', 'felipe.alves@email.com'),
('Gabriela Torres', 'gabriela.torres@email.com'),
('Henrique Costa', 'henrique.costa@email.com'),
('Isabela Duarte', 'isabela.duarte@email.com'),
('João Pedro', 'joao.pedro@email.com');


INSERT INTO alunos (nome, curso) VALUES
('Lucas Oliveira', 'Engenharia Civil'),
('Mariana Lima', 'Medicina'),
('Rafael Martins', 'Administração'),
('Bianca Santos', 'Psicologia'),
('Thiago Gomes', 'Direito'),
('Fernanda Costa', 'Arquitetura'),
('Pedro Henrique', 'Computação'),
('Larissa Almeida', 'Educação Física'),
('Guilherme Souza', 'Matemática'),
('Amanda Ferreira', 'Biologia');








====================================================
Códigos Aula
====================================================
'''
from fastapi import FastAPI
import mysql.connector as my
from pydantic import BaseModel

app = FastAPI()

class UsuarioInput(BaseModel):
    nome:str
    email:str

class AtualizaNome(BaseModel):
    id:int
    nome:str

def conectar_banco():
    config = { 
    'user': 'root', 
    'password': '1234', 
    'host': 'localhost', 
    'database': 'loja_api', 
    }
    conexao = my.connect(**config)
    return conexao

@app.get("/usuarios")
def paginaInicial():
    print(id)
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from usuarios'
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

@app.post("/novousuario")
def novousuario(usuario:UsuarioInput):
    print(usuario.nome)
    print(usuario.email)
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'insert into usuarios (nome, email) values (%s,%s)'
    cursor.execute(sql,(usuario.nome,usuario.email))
    conexao.commit()
    conexao.close()
    return {'msg':'dados enviados com sucesso!!'}


@app.put('/atualizarNome')
def atualizarNome(usuario:AtualizaNome):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'update usuarios set nome = %s where id = %s'
    cursor.execute(sql,(usuario.nome,usuario.id))
    conexao.commit()
    conexao.close()
    return {'msg':'Nome atualizado com sucesso'}

    # dict_aluno = {'nome':'Adriano', 'idade':15}
    # listaAlunos = ['adriano','adriana']
    # tuplaAlunos = ('Cassio','Barbara') 


@app.delete('/deletarUsuario/{id}')
def deletarUsuario(id:int):
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'delete from usuarios where id = %s'
    cursor.execute(sql,(id,))
    conexao.commit()
    conexao.close()
    return {'msg':'Usuario {id} foi deletado com sucesso!!'}

