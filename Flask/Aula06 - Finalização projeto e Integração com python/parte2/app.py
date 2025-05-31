from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def paginaInicial():
    return render_template("index.html")


@app.route("/sobre")
def paginaSobre():
    return render_template('sobre.html')

# app.route("/paginaContato")
# def paginaContato():
#     return '<h1>Essa é a página de contato</h1>'


if __name__ == '__main__':
    app.run(debug=True)