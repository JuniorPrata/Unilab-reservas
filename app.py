from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'some_secret_key'

# Lista de usuários válidos
usuarios_validos = [
    {"nome": "66082", "senha": "30071999"},
    {"nome": "67523", "senha": "67523"},
    {"nome": "usuario2@example.com", "senha": "Senha456"},
    {"nome": "usuario3@example.com", "senha": "Senha789"}
]

# Lista para armazenar reservas
reservas = []

def validar_usuario(nome, senha):
    # Verifica se o nome e senha fornecidos estão na lista de usuários válidos
    for usuario in usuarios_validos:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            return True
    return False

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        if validar_usuario(nome, senha):
            return redirect(url_for('pagina_principal'))
        else:
            return render_template('login.html', erro="E-mail ou senha inválidos.")
    return render_template('login.html', erro=None)

@app.route('/pagina_principal')
def pagina_principal():
    current_date = datetime.now().strftime("%d/%m/%Y")
    return render_template('index.html', reservas=reservas, current_date=current_date)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/lab')
def lab():
    return render_template('lab.html')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        lab = request.form['lab']
        date = request.form['date']
        time = request.form['time']
        reservas.append({"lab": lab, "date": date, "time": time})
        flash('Reserva realizada com sucesso!')
        return redirect(url_for('pagina_principal'))
    return render_template('reserva.html')

@app.route('/labs')
def labs():
    return render_template('labs.html')

if __name__ == '__main__':
    app.run(debug=True)

