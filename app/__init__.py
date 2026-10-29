from flask import Flask

from app import config
from app import db
from app.auth import usuario_atual
from app.routes import auth
from app.routes import main


def create_app():
    app = Flask(__name__, static_url_path="")
    app.config.from_object(config)

    db.init_app(app)

    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)

    @app.context_processor
    def usuario_logado():
        return {"usuario": usuario_atual()}

    return app
