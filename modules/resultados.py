import sqlite3

def adicionar_resultado(id_amostra, descricao, status):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO resultados (id_amostra, descricao, status)
        VALUES (?, ?, ?)
    """, (id_amostra, descricao, status))
    conexao.commit()
    conexao.close()
    print(f"✅ Resultado para amostra {id_amostra} adicionado com sucesso.")

def listar_resultados():
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT r.id_resultado, a.tipo_material, r.descricao, r.status 
        FROM resultados r
        LEFT JOIN amostras a ON r.id_amostra = a.id_amostra
    """)
    for linha in cursor.fetchall():
        print(linha)
    conexao.close()

def buscar_resultado_por_status(status):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM resultados WHERE status LIKE ?", (f"%{status}%",))
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def atualizar_resultado(id_resultado, descricao, status):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE resultados
        SET descricao=?, status=?
        WHERE id_resultado=?
    """, (descricao, status, id_resultado))
    conexao.commit()
    conexao.close()
    print(f"🔄 Resultado {id_resultado} atualizado com sucesso.")

def remover_resultado(id_resultado):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM resultados WHERE id_resultado=?", (id_resultado,))
    conexao.commit()
    conexao.close()
    print(f"🗑️ Resultado {id_resultado} removido.")