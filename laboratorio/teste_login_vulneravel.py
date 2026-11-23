"""Exemplo intencionalmente vulnerável de laboratório. Não usar em produção."""

import sqlite3


def fazer_login(conexao, usuario, senha):
    """Versão didática vulnerável: não usar em aplicações reais."""
    cursor = conexao.cursor()
    query = (
        f"SELECT * FROM usuarios "
        f"WHERE username = '{usuario}' AND password = '{senha}'"
    )
    cursor.execute(query)
    resultado = cursor.fetchone()
    return "Acesso Permitido!" if resultado else "Acesso Negado."


conexao = sqlite3.connect(":memory:")
try:
    conexao.execute(
        "CREATE TABLE usuarios (username TEXT, password TEXT)"
    )
    conexao.execute(
        "INSERT INTO usuarios VALUES (?, ?)",
        ("aluna_demo", "senha-ficticia"),
    )

    # Caso 1: credenciais válidas permitem acesso.
    resultado_valido = fazer_login(
        conexao, "aluna_demo", "senha-ficticia"
    )
    assert resultado_valido == "Acesso Permitido!"
    print("Teste de credenciais válidas: sucesso")

    # Caso 2: senha incorreta nega acesso.
    resultado_senha_incorreta = fazer_login(
        conexao, "aluna_demo", "senha-errada"
    )
    assert resultado_senha_incorreta == "Acesso Negado."
    print("Teste de senha incorreta: sucesso")

    # Caso 3: SQL Injection didática ignora a verificação da senha.
    resultado_injecao = fazer_login(
        conexao, "' OR 1=1 -- ", "senha-errada"
    )
    assert resultado_injecao == "Acesso Permitido!"
    print("SQL Injection reproduzida: acesso permitido com senha incorreta")
finally:
    conexao.close()
