'''
Arquivos iniciais
========================================================
Projeto
| - main.py (Código do python)
| - .gitignore (.venv)
| - readme.md (Explicação do projeto)
| - requirements.txt -> bibliotecas (fastapi uvicorn mysql-connector-python)
========================================================

Comandos terminal
=======================================================

python -m venv .venv (configurar servidor local)
.\.venv\Scripts\activate (Ativar scripts do servidor local)
pip install fastapi uvicorn mysql-connector-python (instalar as bibliotecas)
uvicorn main:app --reload (iniciar o servidor)
ctrl + c (parar o servidor)

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
