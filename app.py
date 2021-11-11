from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {"texto": "Estudar para a prova", "concluida": False},
    {"texto": "Passear com o cachorro", "concluida": True},
    {"texto": "Estudar mais para a prova", "concluida": False},
]

@app.route('/')
def index():
    return render_template('index.html', lista=tarefas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    texto = request.form['texto']      # <input name="texto"/>
    tarefa = { "texto": texto, "concluida": False }
    tarefas.append(tarefa)

    return redirect('https://5000-brown-lemur-kiu2j61j.ws-us18.gitpod.io/')

app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)