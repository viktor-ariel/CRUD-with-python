from flask import Flask, render_template, request, redirect,url_for
import repositorio

app= Flask(__name__)

@app.route("/")
def home():
    dicionario = repositorio.returnPersonagens()
    return render_template("index.html", dados=dicionario)

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editePersonagem(id):
    if request.method == 'POST':
        #QUER DIZER Q O USER ESTA MANDADO DADOS
        if "excluir" in request.form:
            repositorio.removePersonagem(id)
            return redirect(url_for("home"))
        elif 'salvar' in request.form:
            personagem = {}
            personagem['nome'] = request.form['nome']
            personagem['casa'] = request.form['casa']
            personagem['raca'] = request.form['raca']
            personagem['altura'] = request.form['altura'] 
            personagem['nascimento'] = request.form['nascimento']
            personagem['imagem'] = request.form['imagem']
            
            if id in repositorio.returnPersonagens().keys():
                repositorio.updatePersonagem(id, personagem)
            
            return redirect (url_for("home"))
    
    else:
        personagem = repositorio.returnPersonagem(id)
        personagem["id"]=id
        return render_template("cadastro.html", **personagem) 

@app.route("/personagem", methods=["GET", "POST"]) 
def criar_personagem():
    if request.method == "POST":
        personagem = {}
        personagem['nome'] = request.form['nome']
        personagem['casa'] = request.form['casa']
        personagem['raca'] = request.form['raca']
        personagem['altura'] = request.form['altura'] 
        personagem['nascimento'] = request.form['nascimento']
        personagem['imagem'] = request.form['imagem']
        repositorio.createPersonagem(**personagem)
        return redirect (url_for('home'))
    else:
        return render_template('cadastro.html',id=repositorio.gerar_id())
    
app.run(debug=True)