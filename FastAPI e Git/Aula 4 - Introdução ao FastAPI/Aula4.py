'''
python -m venv .venv
.\.venv\Scripts\activate
pip install fastapi uvicorn


Código Banco de dados
===================================
create database loja2;

use loja2;

create table produtos (
id int primary key auto_increment,
nome varchar(100) not null,
preco decimal(10,2) not null,
quatidade int not null
);

alter table produtos rename column quatidade to quantidade;


insert into produtos (nome,preco,quantidade) values
('Fonte', 3500.00, 10),
('Mouse Pad', 35.50, 80),
('Memória', 200.00, 10),
('Placa mãe', 350.50, 80),
('SSD', 200.00, 10),
('Gabinete', 400.50, 80),
('Placa de vídeo', 3500.00, 10),
('cooler', 35.50, 80);

select * from produtos;


instalação do módulo de conexão com o banco de dados
========================================
pip install mysql-connector-python



função de conexão com o banco de dados
=========================================
'''
import mysql.connector as my

from fastapi import FastAPI
import mysql.connector as my

app = FastAPI()

def conectar_banco():
    config = { 
    'user': 'root', 
    'password': '1234', 
    'host': 'localhost', 
    'database': 'loja2', 
    }
    conexao = my.connect(**config)
    return conexao

def buscar_produtos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from produtos'
    cursor.execute(sql)
    resposta = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resposta
# http://localhost:8000/

#@pip install fastapi uvicorn mysql-connector-python



#https://dontpad.com/python/716/aula16


# Questão
# ==========================================================================
# Você foi contratado para desenvolver uma API de gerenciamento de clientes para uma empresa. Sua tarefa é:

# Criar um banco de dados MySQL chamado empresa.
# Criar uma tabela clientes com os seguintes campos:


# id (chave primária, autoincremento)

# nome (VARCHAR(100), não nulo)

# email (VARCHAR(100), único e não nulo)

# idade (INT, não nulo)

# Inserir 10 clientes na tabela.

# Criar uma API FastAPI que tenha um endpoint /clientes que retorne todos os clientes do banco de dados como dicionários.
# Crie um endpoint /cliente/{id_cliente} que retorne um cliente específico
# Crie um endpoint /infoClientes que retorne o nome e a idade de cada cliente
# Testar a API no navegador para garantir que os dados estão sendo retornados corretamente.