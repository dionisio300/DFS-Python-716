# python -m venv .venv 
# .\.venv\Scripts\activate
# pip install fastapi uvicorn mysql-connector-python 
# uvicorn main:app --reload

import mysql.connector as my
from fastapi import FastAPI
from pydantic import BaseModel

class ShowInput(BaseModel):
    nome:str
    data:str
    descricao:str


app = FastAPI()


def criar_conexao():
    conexao = my.connect(
        host = 'localhost',
        user = 'root',
        password = '1234',
        database = 'eventos_db'
    )
    return conexao

def mostrar_shows():
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from shows'
    cursor.execute(sql)
    resultados = cursor.fetchall()
    print(resultados)
    conexao.close()
    return resultados

def mostrar_show(id):
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    sql = 'select * from shows where id = %s'
    cursor.execute(sql,(id,))
    resultados = cursor.fetchone()
    print(resultados)
    conexao.close()
    return resultados

def inserir_show(nome,data,descricao):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    sql = 'insert into shows (nome, data_show, descricao) values (%s,%s,%s)'
    cursor.execute(sql,(nome,data,descricao))
    conexao.commit()
    conexao.close()
    print('Dados inseidos com sucesso')
    return 'Dados inseidos com sucesso'

def atualizar_show(id,nome,data,descricao):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    sql = 'update shows set nome = %s, data_show = %s, descricao = %s where id = %s'
    cursor.execute(sql,(nome,data,descricao,id))
    conexao.commit()
    conexao.close()
    print('Dados Atualizados')
    return 'dados atualizados'

def deletar_show(id):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    sql = 'delete from shows where id = %s'
    cursor.execute(sql,(id,))
    conexao.commit()
    conexao.close()
    print('Show foi deletado com sucesso!!')
    return 'Show deletado com sucesso!!!'


# inserir_show('Ana Carolina', '2025-07-30','Show em fortaleza')
# atualizar_show(1,'Jquest','2025-11-11','teste')

@app.get('/shows/')
def pagina_inicial():
    return mostrar_shows()


@app.get('/shows/{id}')
def trazer_show(id):
    return mostrar_show(id)

@app.post('/shows')
def cadastrar_show(show:ShowInput):
    return inserir_show(show.nome, show.data, show.descricao)

@app.put('/shows/{id}')
def update_show(id,show:ShowInput):
    return atualizar_show(id,show.nome,show.data,show.descricao)

@app.delete('/shows/{id}')
def del_show(id):
    return deletar_show(id)