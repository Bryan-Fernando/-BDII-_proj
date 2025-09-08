import sqlite3
from config import Config
import os
from werkzeug.security import generate_password_hash

os.makedirs("instance", exist_ok=True)

def get_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS enderecos (
      id_endereco   INTEGER PRIMARY KEY AUTOINCREMENT,
      logradouro    TEXT NOT NULL,
      numero        TEXT NOT NULL,
      complemento   TEXT,
      bairro        TEXT NOT NULL,
      cep           TEXT NOT NULL,
      cidade        TEXT NOT NULL,
      estado        TEXT NOT NULL,
      UNIQUE (logradouro, numero, complemento, bairro, cep, cidade, estado)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
      id_funcionario INTEGER PRIMARY KEY AUTOINCREMENT,
      nome_completo  TEXT NOT NULL,
      cpf            TEXT NOT NULL UNIQUE,
      email          TEXT NOT NULL UNIQUE,
      id_endereco    INTEGER,
      FOREIGN KEY (id_endereco) REFERENCES enderecos(id_endereco)
        ON UPDATE CASCADE ON DELETE SET NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
      id_usuario     INTEGER PRIMARY KEY AUTOINCREMENT,
      id_funcionario INTEGER NOT NULL UNIQUE,
      senha_hash     TEXT NOT NULL,
      ultimo_login   TEXT,
      ativo          INTEGER NOT NULL DEFAULT 1,
      FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario)
        ON UPDATE CASCADE ON DELETE CASCADE
    );
    """)

    cur.execute("""INSERT OR IGNORE INTO enderecos
      (id_endereco, logradouro, numero, complemento, bairro, cep, cidade, estado)
      VALUES (1,'Rua A','123',NULL,'Centro','76800000','Porto Velho','RO');""")

    cur.execute("""INSERT OR IGNORE INTO funcionarios
      (id_funcionario, nome_completo, cpf, email, id_endereco)
      VALUES
      (1, 'João Silva',  '12345678901', 'joao@ifro.edu', 1),
      (2, 'Maria Souza', '98765432100', 'maria@ifro.edu',1);""")

    cur.execute("""INSERT OR IGNORE INTO usuarios
      (id_usuario, id_funcionario, senha_hash)
      VALUES
      (1, 1, ?),
      (2, 2, ?);""", (
        generate_password_hash("Senha@123"), 
        generate_password_hash("Senha@123")
    ))

    conn.commit()
    conn.close()
