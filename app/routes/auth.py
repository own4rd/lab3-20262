from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from app.queries import buscar_usuario_por_email
from app.queries import criar_usuario

bp = Blueprint("auth", __name__)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        usuario = buscar_usuario_por_email(email)
        if usuario is None or not check_password_hash(usuario["senha_hash"], senha):
            flash("E-mail ou senha inválidos.", "danger")
            return render_template("login.html", email=email), 401
        session.clear()
        session["usuario_id"] = usuario["id"]
        flash(f"Bem-vindo(a), {usuario['nome']}!", "success")
        destino = request.args.get("next", "")
        if not destino.startswith("/") or destino.startswith("//"):
            destino = url_for("main.dashboard")
        return redirect(destino)
    return render_template("login.html")

@bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")
        confirmacao = request.form.get("confirmacao", "")

        erro = None
        if not nome or not email or not senha:
            erro = "Preencha todos os campos."
        elif len(senha) < 6:
            erro = "A senha deve ter pelo menos 6 caracteres."
        elif senha != confirmacao:
            erro = "As senhas não conferem."
        elif buscar_usuario_por_email(email):
            erro = "Já existe uma conta com este e-mail."

        if erro:
            flash(erro, "danger")
            return render_template("registro.html", nome=nome, email=email), 400

        criar_usuario(nome, email, generate_password_hash(senha))
        flash("Conta criada com sucesso! Faça login para continuar.", "success")
        return redirect(url_for("auth.login"))
    return render_template("registro.html")

@bp.post("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("main.home"))
