from pathlib import Path

import click
import psycopg
from flask import current_app
from flask import g
from psycopg.rows import dict_row


def get_db():
    """Abre uma conexão por requisição e reaproveita até o fim dela."""
    if "db" not in g:
        g.db = psycopg.connect(current_app.config["DATABASE_URL"], row_factory=dict_row)
    return g.db


def close_db(erro=None):
    conexao = g.pop("db", None)
    if conexao is not None:
        if erro is None:
            conexao.commit()
        else:
            conexao.rollback()
        conexao.close()


def consultar(sql, params=(), um=False):
    with get_db().cursor() as cur:
        cur.execute(sql, params)
        return cur.fetchone() if um else cur.fetchall()


def executar(sql, params=()):
    with get_db().cursor() as cur:
        cur.execute(sql, params)
    get_db().commit()


@click.command("init-db")
def init_db():
    """Cria as tabelas e insere os produtos iniciais."""
    schema = (Path(__file__).parent / "schema.sql").read_text()
    with psycopg.connect(current_app.config["DATABASE_URL"]) as conexao:
        conexao.execute(schema)
    click.echo("Banco de dados inicializado.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db)
