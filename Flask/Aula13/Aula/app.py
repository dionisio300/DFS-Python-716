from flask import Flask, render_template, request, redirect, session
import mysql.connector as my

app = Flask(__name__)
app.secret_key = '12345'


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
        try:
            if senha == usuario_buscado["senha"]:
                print('Usuário pode entrar')

                session["nome"] = usuario_buscado["nome"]
                session["tipo"] = usuario_buscado["tipo"]
                session["logado"] = True


                if usuario_buscado["tipo"] == 'administrador':
                    return redirect('paginaAdm')
                elif usuario_buscado["tipo"] == 'cliente':
                    return redirect('paginaCliente')
                elif usuario_buscado["tipo"] == 'usuario':
                    return redirect('paginaUsuario')

            elif senha != usuario_buscado["senha"]:
                print('Usuário erro a senha, tente novamente!')
        except:
            print('erro ao trazer do banco de dados')
        

        print(usuario_buscado)
        return render_template('login.html')


@app.get('/paginaAdm')
def administrador():
    if 'tipo' not in session:
        return redirect('login')
    
    if session['tipo'] == 'administrador':
        return render_template('administrador.html')
    else:
        return redirect('login')
        

@app.get('/paginaCliente')
def cliente():
    if 'tipo' not in session:
        return redirect('login')
    if session['tipo'] == 'cliente':
        return render_template('cliente.html')
    else:
        return redirect('login')

@app.get('/paginaUsuario')
def usuario():
    if 'tipo' not in session:
        return redirect('login')
    if session['tipo'] == 'usuario':
        #Aqui vai o código para essa página

        return render_template('usuario.html')
    else:
        return redirect('login')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html') 
    elif request.method == 'POST':
        nome = request.form.get('name')
        nome_usuario = request.form.get('username')
        email = request.form.get('email')
        tipo = request.form.get('accountType')
        senha = request.form.get('senha')
        print(f'Name: {nome}, Username: {nome_usuario}, AccountType: {tipo}, E-mail: {email}, Senha: {senha}')
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql_verificacao = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(sql_verificacao, (email,))
        usuario_buscado = cursor.fetchone()
        if usuario_buscado:
            return "E-mail já cadastrado. Tente outro."
        sql_insercao = """
            INSERT INTO usuarios (nome, nome_usuario, email, tipo, senha)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql_insercao, (nome, nome_usuario, email, tipo, senha))
        conexao.commit()
        cursor.close()
        conexao.close()

        return "Usuário cadastrado com sucesso"

    
 
app.run(debug=True)


# criar a rota
# criar o template
# pegar as informações do formulário e levar para o python

app.run(debug=True)


