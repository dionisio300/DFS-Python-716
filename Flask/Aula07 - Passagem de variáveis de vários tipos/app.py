from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/listarEventos')
def paginaListarEventos():
    return render_template('listarEventos.html')

@app.route('/paginaConsultar', methods = ['get','post'])
def paginaConsultar():

    mostrarResultado = False

    dadosEvento = [{
        "nome":'Show de Samba',
        "data":'02/05/2026',
        "local":"Praia",
        "hora": '20:00',
        "lotacao": 3000,
        "ingressosVendidos":2635,
        "ingressosDisponiveis":365
    },{
        "nome":'Show de Rock',
        "data":'02/05/2026',
        "local":"Praia",
        "hora": '20:00',
        "lotacao": 3000,
        "ingressosVendidos":2635,
        "ingressosDisponiveis":365
    },{
        "nome":'Show de MPB',
        "data":'02/05/2026',
        "local":"Praia",
        "hora": '20:00',
        "lotacao": 3000,
        "ingressosVendidos":2635,
        "ingressosDisponiveis":365
    }]
    resultadoEvento = {}
    if request.method == 'POST':
        id = int(request.form.get('id_busca'))
        mostrarResultado = True
        resultadoEvento = dadosEvento[id]
        print(id)
    
    return render_template('consultarEventos.html',dadosEvento=resultadoEvento, mostrarResultado = mostrarResultado)
# mostrarResultado = True
    # nome = 'Show de Samba'
    # data = '02/05/2026'
    # local = 'Praia'
    # hora = '20:00'
    # lotacao = 3000
    # ingressosVendidos = 2635
    # ingressosDisponiveis = lotacao - ingressosVendidos

    # return render_template('consultarEventos.html',nome = nome,data = data,local = local,hora = hora,lotacao = lotacao, ingressosVendidos = ingressosVendidos, ingressosDisponiveis = ingressosDisponiveis,mostrarResultado=mostrarResultado)

    # Youth Alunos
    # senha: Youthalunos*.

@app.route('/paginaCadastrar')
def paginaCadastrar():
    return render_template('paginaCadastrar.html')

@app.route('/paginaAtualizar')
def paginaAtualizar():
    return render_template('paginaAtualizar.html')

if __name__ == '__main__':
    app.run(debug=True)