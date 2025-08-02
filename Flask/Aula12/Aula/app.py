from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')
        lembrar = request.form.get('lembrar')

        print(f'E-mail: {email}, Senha: {senha}, Lembrar: {lembrar}')

        return render_template('login.html')





app.run(debug=True)
