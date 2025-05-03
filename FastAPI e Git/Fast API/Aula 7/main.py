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



