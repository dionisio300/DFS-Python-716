from flask import Flask, render_template, request

app = Flask(__name__)

dadosEvento = [{
        "nome":'Show de Samba',
        "data":'2026-05-02',
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

@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/listarEventos')
def paginaListarEventos():
    return render_template('listarEventos.html',eventos=dadosEvento)

@app.route('/paginaDeletar', methods = ['get','post'])
def paginaDeletar():
    if request.method=='POST':
        id = int(request.form.get('id'))
        dadosEvento.pop(id)
        return render_template('deletarEvento.html')
    return render_template('deletarEvento.html')

@app.route('/paginaConsultar', methods = ['get','post'])
def paginaConsultar():
    mostrarResultado = False
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

@app.route('/paginaCadastrar', methods = ['get','post'])
def paginaCadastrar():
    if request.method == 'POST':
       nome = request.form.get('nome')
       data = request.form.get('data')
       local = request.form.get('local')
       hora = request.form.get('hora')
       lotacao = int(request.form.get('lotacao'))
       ingressosVendidos = 0
       ingressosDisponiveis = lotacao - ingressosVendidos
       
       novoEvento = {
           "nome":nome,
           "data":data,
           "local":local,
           "hora":hora,
           "lotacao":lotacao,
           "ingressosVendidos":ingressosVendidos,
           "ingressosDisponiveis":ingressosDisponiveis
       }

       dadosEvento.append(novoEvento)
       print(dadosEvento)

       print(nome,data,local,hora,lotacao)

    return render_template('paginaCadastrar.html')

@app.route('/paginaAtualizar', methods = ['get','post'])
def paginaAtualizar():
    mostrarEvento = False
    if request.method == 'POST':
        id = int(request.form.get('id'))
        eventoSelecionado = dadosEvento[id]
        mostrarEvento = True
        return render_template('paginaAtualizar.html',eventoSelecionado = eventoSelecionado, mostrarEvento = mostrarEvento, id = id)
    return render_template('paginaAtualizar.html',mostrarEvento = mostrarEvento)

@app.route('/atualizarEvento', methods = ['get','post'])
def atualizarEvento():
    mostrarEvento = False
    if request.method == 'POST':
        novoNome = request.form.get('nome')
        novaData = request.form.get('data')
        novoLocal = request.form.get('local')
        novaHora = request.form.get('hora')
        novaLotacao = request.form.get('lotacao')
        id = int(request.form.get('id_evento'))
        print(novoNome,novaData,novoLocal,novaHora,novaLotacao,id)

        dadosEvento[id] = {"nome":novoNome,"data":novaData,"local":novoLocal,"hora":novaHora,"lotacao":novaLotacao}

        return render_template('paginaAtualizar.html',mostrarEvento = mostrarEvento)
    
    return render_template('paginaAtualizar.html',mostrarEvento = mostrarEvento)




if __name__ == '__main__':
    app.run(debug=True)