from flask import Flask, render_template, request, redirect
import mysql.connector as my
app = Flask(__name__)

# terminal: pip install mysql-connector-python

# função para conectar ao banco de dados
def conectar_banco():
    conexao = my.connect(
        host="localhost",
        user="root",
        password="1234",
        database="eventos"
    )
    return conexao

# testar conexão
conexao = conectar_banco()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    elif request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        lembrar = request.form.get('lembrar')

        print(f'E-mail: {email}, Senha: {senha}, Lembrar: {lembrar}')
        # Aqui você pode adicionar lógica para verificar o usuário no banco de dados
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql = "select * from usuarios where email = %s"
        cursor.execute(sql,(email,))
        usuario_buscado = cursor.fetchone()

        

        print(usuario_buscado)
        return render_template('login.html')





app.run(debug=True)
