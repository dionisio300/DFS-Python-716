from flask import Flask, request, url_for,render_template

import mysql.connector as my

app = Flask(__name__)

def conectarBanco():
    conexao = my.connect(
        host="localhost",
        user="root",
        password="1234",
        database="loja123"
    )
    return conexao
conectarBanco()
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    senha = request.form.get('senha')
    print(f'Usuário: {user} - Senha: {senha}')

    conexao = conectarBanco()
    


    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)