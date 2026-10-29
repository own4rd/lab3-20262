from app.db import consultar
from app.db import executar


def listar_produtos():
    return consultar("SELECT id, nome, preco FROM produtos ORDER BY id")


def buscar_produto(id):
    return consultar("SELECT id, nome, preco FROM produtos WHERE id = %s", (id,), um=True)


def buscar_usuario_por_id(id):
    return consultar("SELECT id, nome, email, senha_hash FROM usuarios WHERE id = %s", (id,), um=True)


def buscar_usuario_por_email(email):
    return consultar("SELECT id, nome, email, senha_hash FROM usuarios WHERE email = %s", (email,), um=True)


def criar_usuario(nome, email, senha_hash):
    executar(
        "INSERT INTO usuarios (nome, email, senha_hash) VALUES (%s, %s, %s)",
        (nome, email, senha_hash),
    )


def contar_usuarios():
    return consultar("SELECT COUNT(*) AS total FROM usuarios", um=True)["total"]
