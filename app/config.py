import os

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://loja:loja@localhost:5432/loja",
)
