
from flask import render_template, request
from config import app
from flask import jsonify
import repository

@app.route('/')
def categorias():
    categorias  = repository.get_categorias()    
    _, _, qtd_total = repository.get_carrinho()
    return render_template("index.html", categorias = categorias, qtd_carrinho = qtd_total)

@app.route('/categoria/<id_categoria>')
def sorvetes_por_categoria(id_categoria):
    sorvetes  = repository.get_sorvetes_by_categoria(id_categoria)
    _, _, qtd_total  = repository.get_carrinho()
    return render_template("sorvetes.html", sorvetes = sorvetes, qtd_carrinho = qtd_total)

@app.route('/cesta')
def cesta_compras():
    carrinho, total, _ = repository.get_carrinho()
    return render_template("cesta_compras.html", carrinho = carrinho, total = total)

@app.post('/cesta/add')
def add_item_carrinho():
    data = request.json
    sorvete = repository.get_sorvetes_by_id(data['id'])
    carrinho = repository.add_item_carrinho(sorvete, data['qtd'])
    return jsonify(carrinho)

@app.delete('/cesta/<sorvete_id>')
def remove_item_carrinho(sorvete_id):
    carrinho = repository.remove_item_carrinho(sorvete_id)
    return jsonify(carrinho)

if __name__ == "__main__":
    app.run(debug=True)