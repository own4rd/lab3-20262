from flask import Flask
from flask import render_template

app = Flask(__name__,
    static_url_path='',
    static_folder='static')


@app.get("/")
def home():

    produtos = [
        {
            "nome": "Produto 1",
            "preco": 299.99
        },
        {
            "nome": "Produto 2",
            "preco": 302.99
        },
        {
            "nome": "Produto 3",
            "preco": 49.99
        },
    ]
    return render_template("home.html", produtos=produtos)

@app.get("/sobre")
def about():
    return render_template("about.html")
