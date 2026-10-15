from flask import Flask
from flask import abort
from flask import render_template

app = Flask(__name__,
    static_url_path='',
    static_folder='static')


produtos = [
    {
        "id": 1,
        "nome": "Produto 1",
        "preco": 299.99
    },
    {
        "id": 2,
        "nome": "Produto 2",
        "preco": 302.99
    },
    {
        "id": 3,
        "nome": "Produto 3",
        "preco": 49.99
    },
]


@app.get("/")
def home():
    return render_template("home.html", produtos=produtos)

@app.get("/sobre")
def about():
    return render_template("about.html")

@app.get("/produto/<int:id>")
def produto(id):
    produto = next((p for p in produtos if p["id"] == id), None)
    if produto is None:
        abort(404)
    return render_template("produto.html", produto=produto)
