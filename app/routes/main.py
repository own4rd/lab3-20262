from flask import Blueprint
from flask import abort
from flask import render_template

from app.auth import login_obrigatorio
from app.queries import buscar_produto
from app.queries import contar_usuarios
from app.queries import listar_produtos

bp = Blueprint("main", __name__)


@bp.get("/")
def home():
    return render_template("home.html", produtos=listar_produtos())

@bp.get("/sobre")
def about():
    return render_template("about.html")

@bp.get("/produto/<int:id>")
def produto(id):
    produto = buscar_produto(id)
    if produto is None:
        abort(404)
    return render_template("produto.html", produto=produto)

@bp.get("/dashboard")
@login_obrigatorio
def dashboard():
    produtos = listar_produtos()
    total = sum(p["preco"] for p in produtos)
    resumo = {
        "quantidade": len(produtos),
        "total": total,
        "media": total / len(produtos) if produtos else 0,
        "usuarios": contar_usuarios(),
    }
    return render_template("dashboard.html", produtos=produtos, resumo=resumo)
