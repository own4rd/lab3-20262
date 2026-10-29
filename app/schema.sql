CREATE TABLE IF NOT EXISTS usuarios (
    id         SERIAL PRIMARY KEY,
    nome       VARCHAR(120) NOT NULL,
    email      VARCHAR(255) NOT NULL UNIQUE,
    senha_hash VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS produtos (
    id    SERIAL PRIMARY KEY,
    nome  VARCHAR(120)   NOT NULL,
    preco NUMERIC(10, 2) NOT NULL
);

INSERT INTO produtos (nome, preco)
SELECT * FROM (VALUES
    ('Produto 1', 299.99),
    ('Produto 2', 302.99),
    ('Produto 3', 49.99)
) AS iniciais
WHERE NOT EXISTS (SELECT 1 FROM produtos);
