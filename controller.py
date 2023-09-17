
from flask import render_template
from config import app
import repository

@app.route('/')
def categorias():
    categorias  = repository.get_categorias()    
    return render_template("index.html", categorias = categorias)

@app.route('/categoria/<id_categoria>')
def sorvetes_por_categoria(id_categoria):
    sorvetes  = repository.get_sorvetes_by_categoria(id_categoria)    
    return render_template("sorvetes.html", sorvetes = sorvetes)



if __name__ == "__main__":
    app.run(debug=True)