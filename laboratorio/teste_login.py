import sqlite3


def fazer_login(conexao, usuario, senha):
    """Versão corrigida com consulta parametrizada."""
    cursor = conexao.cursor()
    query = "SELECT * FROM usuarios WHERE username = ? AND password = ?"
    cursor.execute(query, (usuario, senha))
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

    # Caso 3: a entrada de SQL Injection é tratada como dado literal.
    resultado_injecao = fazer_login(
        conexao, "' OR 1=1 -- ", "senha-errada"
    )
    assert resultado_injecao == "Acesso Negado."
    print("SQL Injection bloqueada: acesso negado")
finally:
    conexao.close()
