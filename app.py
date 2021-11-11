from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {"texto": "Estudar para a prova", "concluida": False},
    {"texto": "Passear com o cachorro", "concluida": True},
    {"texto": "Estudar mais para a prova", "concluida": False},
    {"texto": "Estudar para a prova", "concluida": True},
]

@app.route('/')
def index():
    return render_template('index.html', lista=tarefas)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    texto = request.form['texto']  
    status = request.form['status']    # <input name="texto"/>
    tarefa = { "texto": texto, "concluida": status }
    tarefas.append(tarefa)

    return redirect('https://5000-cyan-pig-k8e57iy3.ws-us18.gitpod.io/')

@app.route('/busca', methods=['POST'])
def pes():
    result = []
    resultado = request.form['pesquisa']
    for i in tarefas:
        if resultado in i['texto']:            
            result.append(i)     

    if not result:
        return render_template('erro.html')

    return render_template('busca.html', lista2=result)  



        
app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)   
# Implementar uma pesquisa (3,0 pontos)

