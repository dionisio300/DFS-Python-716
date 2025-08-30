from flask import Flask,render_template,url_for,request
import requests

app = Flask(__name__)

@app.route('/')
def index():

    url = f'https://fakestoreapi.com/products'
    resposta = requests.get(url)
    dados = ''
    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados)

        return render_template('todosProdutos.html',dados = dados)
    
    return render_template('todosProdutos.html',dados = dados)

@app.route('/<id>')
def paginaInicial(id:int):

    print(id)

    url = f'https://fakestoreapi.com/products/{id}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados)

        return render_template('index.html',dados = dados)

    return render_template('index.html')

@app.route('/paginaCompra/<id>')
def paginaCompra(id:int):
    url = f'https://fakestoreapi.com/products/{id}'
    resposta = requests.get(url)
    dados = ''
    parcela = ''
    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados)
        preco = dados['price']
        parcela = preco/12
        parcela = round(parcela,2)
        print(parcela)

        return render_template('paginaCompra.html', dados=dados, parcela = parcela)

    return render_template('paginaCompra.html',dados = dados, parcela = parcela)










app.run(debug=True)