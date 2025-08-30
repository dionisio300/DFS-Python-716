from flask import Flask, request, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    dados = []
    return render_template('index.html',dados = dados)

@app.route('/mostrarEndereco', methods = ['GET','POST'])
def mostrarEndereco():

    if request.method == 'POST':
        
        nome = request.form.get('nome')
        cep = request.form.get('cep')
        # Criar a URL da API
        url = f'https://viacep.com.br/ws/{cep}/json/'
        # Fazer a chamada da API
        resposta = requests.get(url)
        # Validação da resposta
        if resposta.status_code == 200:
            dados = resposta.json()
            print(dados)
            if 'erro' in dados:
                return render_template('paginaErro.html')
            else:
                return render_template('index.html', dados=dados,nome=nome)
        else:
            erro = resposta.status_code
            return render_template('paginaErro.html')
    else:
        return render_template('index.html')







app.run(debug=True)