from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        # Autenticação aqui...
        return redirect(url_for('index'))
    return render_template('login.html')


@app.route('/cadastro')
def cadastro():
    return 'Página de Cadastro'

app.run(debug=True)