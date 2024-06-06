from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Lista de usuários válidos
usuarios_validos = [
    {"nome": "66082", "senha": "30071999"},
    {"nome": "usuario1@example.com", "senha": "Senha123"},
    {"nome": "usuario2@example.com", "senha": "Senha456"},
    {"nome": "usuario3@example.com", "senha": "Senha789"}
]

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
    reservations = [
        {"info": "João, Física, 10:00-11:00", "top": 50, "height": 30},
        {"info": "Maria, Matemática, 11:00-12:00", "top": 100, "height": 30},
        # Adicione mais reservas conforme necessário
    ]
    current_date = datetime.now().strftime("%d/%m/%Y")
    return render_template('index.html', reservations=reservations, current_date=current_date)

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
