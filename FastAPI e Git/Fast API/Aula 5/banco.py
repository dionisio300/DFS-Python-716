import mysql.connector as my

config = { 
  'user': 'root', 
  'password': '1234', 
  'host': 'localhost', 
  'database': 'loja2', 
}

conexao = my.connect(**config)

# Criando um cursor para executar queries 
cursor = conexao.cursor(dictionary=True) 

sql = 'select * from produtos'
cursor.execute(sql)
resposta = cursor.fetchall()
print(resposta)