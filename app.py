from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = [
    {"texto": "Camaro 2012", "concluida": "R$ 80.000,00"},
    {"texto": "Uno 1994", "concluida": "R$ 12.000,00"},
    {"texto": "Nissan Skyline 1992", "concluida": "R$ 120.000,00"},
    {"texto": "Ferrari Roma 2022", "concluida": "R$ 3.300.000,00"},
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

    return render_template('index.html', lista=tarefas)

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

@app.route('/deletar', methods=['POST'])
def delete():
    item_deletar = request.form['deletar']
    cont = 0
    for i in tarefas:
        if item_deletar == i['texto']:       
            tarefas.remove(i)
            return render_template('index.html', lista=tarefas)
            
    
    
    return render_template('erro.html')

    
    
    

@app.route('/gerar')
def gerador():
    return render_template('delete.html')

        
app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)   
# Implementar uma pesquisa (3,0 pontos)

