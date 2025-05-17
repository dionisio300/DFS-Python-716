from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    nome = 'Dionizio'
    idade = 28
    return render_template('index.html', name = nome, age = idade)


@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')


if __name__ == '__main__':
    app.run(debug=True)