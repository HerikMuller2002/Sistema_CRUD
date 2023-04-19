import sqlite3
# import sys
# import os

# # Obtém o diretório pai do diretório atual
# diretorio_pai = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# # Adiciona o diretório ao sys.path
# sys.path.insert(0, diretorio_pai)


def create_acces(email, senha):
    # Abre a conexão com o banco de dados
    conn = sqlite3.connect('Dash\\database\\banco.db')
    cursor = conn.cursor()
    # Executa a query de inserção dos dados na tabela de login
    cursor.execute("INSERT INTO login (user, password) VALUES (?, ?)", (email, senha))
    # Realiza o commit da transação
    conn.commit()
    # Fecha a conexão com o banco de dados
    conn.close()

def verify_acces(email, senha):
    # Abre a conexão com o banco de dados
    conn = sqlite3.connect('Dash\\database\\banco.db')
    cursor = conn.cursor()
    # Executa a query de consulta dos dados na tabela de login
    cursor.execute("SELECT id FROM login WHERE user = ? AND password = ?", (email, senha))
    # Recupera o resultado da consulta
    resultado = cursor.fetchone()
    # Fecha a conexão com o banco de dados
    conn.close()
    # Retorna o resultado da consulta
    return resultado