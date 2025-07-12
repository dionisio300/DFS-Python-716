from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def paginaInicial():
    return render_template('index.html')

@app.route('/grid')
def grid():
    return render_template('sistemaGridsBootstrap.html')

@app.route('/exemplo1')
def exemplo():
    return render_template('exemplo1.html')


if __name__ == '__main__':
    app.run(debug=True)