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

@app.get("/produtos/{qtd_produtos}")
def read_root(qtd_produtos:int):
    
    produtos = buscar_produtos()
    
    listaProdutos = []

    for i in range (qtd_produtos):
        listaProdutos.append(produtos[i])

    return listaProdutos


@app.get("/produto/{id_produto}")
def read_root(id_produto:int):
    
    produtos = buscar_produtos()
    return produtos[id_produto - 1]



