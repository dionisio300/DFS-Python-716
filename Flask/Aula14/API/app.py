from flask import Flask, request, redirect, url_for, render_template
import requests

app = Flask(__name__)

@app.route('/')
def paginaInicial():

    return render_template('index.html')

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
            # Trazer os dados vindos da API para a variável dados
            dados = resposta.json()

            if dados['erro']:
                print('Erro')
                return render_template('index.html',nome=nome,cep=cep,resposta = 'erro')
            else:
                # Enviando os dados para a página HTML
                return render_template('index.html',nome=nome,cep=cep,resposta = dados)
        else:
            erro = resposta.status_code
            return render_template('index.html', erro=erro)
    else:
        return render_template('index.html')

app.run(debug=True)