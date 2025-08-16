from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector as my
import bcrypt

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
            if bcrypt.checkpw(senha.encode('utf-8'), usuario_buscado["senha"].encode('utf-8')):
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
                errou = True
                return render_template('login.html',errou = errou)
        except Exception as e:
            return render_template('erro.html',erro = e)
        

        print(usuario_buscado)
        return render_template('login.html')


@app.get('/paginaAdm')
def administrador():
    if 'tipo' not in session:
        return redirect('login')
    if session['tipo'] == 'administrador':
        tipo = session['tipo']
        nome = session['nome']
        return render_template('administrador.html',nome = nome,tipo = tipo)
    else:
        return redirect('login')
        

@app.get('/paginaCliente')
def cliente():
    if 'tipo' not in session:
        return redirect('login')
    if session['tipo'] == 'cliente':

        tipo = session['tipo']
        nome = session['nome']

        return render_template('cliente.html',nome = nome,tipo = tipo)
    else:
        return redirect('login')

@app.get('/paginaUsuario')
def usuario():
    if 'tipo' not in session:
        return redirect('login')
    if session['tipo'] == 'usuario':
        
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql = 'select * from eventos'
        cursor.execute(sql)
        eventos = cursor.fetchall()

        tipo = session['tipo']
        nome = session['nome']


        return render_template('usuario.html', eventos = eventos,nome = nome,tipo = tipo)
    else:
        return redirect('login')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html') 
    elif request.method == 'POST':
        nome = request.form.get('nome')
        userName = request.form.get('username')
        email = request.form.get('email')
        tipo = request.form.get('tipo')
        senha = request.form.get('senha')

        senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        print(f'Senha: {senha}')

        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        sql = 'select * from usuarios where email = %s'
        cursor.execute(sql,(email,))
        usuario = cursor.fetchone()

        if usuario:
            print(f'Usuario já cadastrado')
            cadastrado = True
            return render_template('cadastro.html', cadastrado = cadastrado,nome = nome)
        else:
            try:
                sql = 'insert into usuarios (nome, nome_usuario, senha, email, tipo) values (%s,%s,%s,%s,%s)'
                cursor.execute(sql,(nome,userName,senha,email,tipo))
                conexao.commit()
                conexao.close()
                return render_template('confirmaCadastro.html')
            except Exception as e:
                return render_template('erro.html',erro = e)

        
    
 
@app.route('/sair')
def sair():
    session.clear()
    return redirect(url_for('home'))

@app.route('/eventoS', methods=['GET', 'POST'])
def eventoS():
    if request.method == 'GET':
        return render_template('eventoS.html')
    if request.method == 'POST':
        id = request.form.get('id')
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        local_evento = request.form.get('local_evento')
        horario = request.form.get('horario')
        lotacao = request.form.get('lotacao')
        ingressos_disponiveis = request.form.get('ingressos_disponiveis')

        evento = {
            'id':id,
            'titulo':titulo,
            'descricao':descricao,
            "local_evento":local_evento,
            "horario":horario,
            "lotacao" :lotacao,
            "ingressos_disponiveis":ingressos_disponiveis
        }

        return render_template('eventoS.html',evento=evento)

# criar a rota
# criar o template
# pegar as informações do formulário e levar para o python

app.run(debug=True)