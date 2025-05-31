from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    print('teste')
    return render_template('index.html')


@app.route("/sobre")
def paginaSobre():
    return render_template('sobre.html')

@app.route('/paginaContato')
def paginaContato():
    
    return render_template('paginaContato.html')

@app.route('/paginaContato/<int:num>')
def paginaContatoEspecifico(num):
    funcionarios = [
        {"id":1, "nome":"Maria", "funcao":"Analista"},
        {"id":2, "nome":"Pedro", "funcao":"Suporte"},
    ]
    mensagem = ''
    for funcionario in funcionarios:
        if funcionario["id"] == num:
            mensagem = f'Essa é a págiana de contato do(a) {funcionario["nome"]}'
    
    return mensagem


@app.route('/paginaContato/<nome>')
def paginaContatoNome(nome):
    mensagem = f'Olá {nome} existe um cliente querendo falar com você!!'

    return mensagem

@app.route('/paginaChamado')
def paginaChamado():
    funcionario = 'Caio'
    suporte = 'Pedro'
    descricao = 'O computador está se desligando sozinho!!'

    return render_template('chamado.html',funcionario = funcionario,suporte = suporte,descricao = descricao)



if __name__ == '__main__':
    app.run(debug=True)