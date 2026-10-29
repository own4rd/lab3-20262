from functools import wraps

from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import url_for

from app.queries import buscar_usuario_por_id


def usuario_atual():
    usuario_id = session.get("usuario_id")
    return buscar_usuario_por_id(usuario_id) if usuario_id else None


def login_obrigatorio(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Faça login para acessar esta página.", "warning")
            return redirect(url_for("auth.login", next=request.path))
        return view(*args, **kwargs)
    return wrapper
