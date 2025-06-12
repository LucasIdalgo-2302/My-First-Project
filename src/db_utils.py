import sqlite3
import pandas as pd

def conectar_db(nome_banco="alunos.db"):
    return sqlite3.connect(nome_banco)

def criar_tabela(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            aluno TEXT,
            idade INTEGER,
            nota REAL
        );
    """)
    conn.commit()

def inserir_dados(conn, df):
    df.to_sql("alunos", conn, if_exists="replace", index=False)

def ler_dados(conn):
    return pd.read_sql("SELECT * FROM alunos", conn)
