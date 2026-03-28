import sqlite3

def adicionar_pesquisador(nome, especialidade, email):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pesquisadores (nome, especialidade, email) VALUES (?, ?, ?)", 
                   (nome, especialidade, email))
    conexao.commit()
    conexao.close()
    print(f"✅ Pesquisador '{nome}' adicionado com sucesso!")

def listar_pesquisadores():
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pesquisadores")
    for linha in cursor.fetchall():
        print(linha)
    conexao.close()

def buscar_pesquisador_por_nome(nome):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pesquisadores WHERE nome LIKE ?", (f"%{nome}%",))
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def atualizar_pesquisador(id_pesquisador, nome, especialidade, email):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE pesquisadores 
        SET nome=?, especialidade=?, email=? 
        WHERE id_pesquisador=?
    """, (nome, especialidade, email, id_pesquisador))
    conexao.commit()
    conexao.close()
    print(f"🔄 Pesquisador {id_pesquisador} atualizado com sucesso.")

def remover_pesquisador(id_pesquisador):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM pesquisadores WHERE id_pesquisador=?", (id_pesquisador,))
    conexao.commit()
    conexao.close()
    print(f"🗑️ Pesquisador {id_pesquisador} removido.")