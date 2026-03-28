import sqlite3

def adicionar_amostra(tipo_material, data_coleta, id_pesquisador):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO amostras (tipo_material, data_coleta, id_pesquisador)
        VALUES (?, ?, ?)
    """, (tipo_material, data_coleta, id_pesquisador))
    conexao.commit()
    conexao.close()
    print(f"✅ Amostra '{tipo_material}' cadastrada com sucesso.")

def listar_amostras():
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT a.id_amostra, a.tipo_material, a.data_coleta, p.nome 
        FROM amostras a
        LEFT JOIN pesquisadores p ON a.id_pesquisador = p.id_pesquisador
    """)
    for linha in cursor.fetchall():
        print(linha)
    conexao.close()

def buscar_amostra_por_tipo(tipo_material):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM amostras WHERE tipo_material LIKE ?", (f"%{tipo_material}%",))
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def atualizar_amostra(id_amostra, tipo_material, data_coleta, id_pesquisador):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE amostras
        SET tipo_material=?, data_coleta=?, id_pesquisador=?
        WHERE id_amostra=?
    """, (tipo_material, data_coleta, id_pesquisador, id_amostra))
    conexao.commit()
    conexao.close()
    print(f"🔄 Amostra {id_amostra} atualizada com sucesso.")

def remover_amostra(id_amostra):
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM amostras WHERE id_amostra=?", (id_amostra,))
    conexao.commit()
    conexao.close()
    print(f"🗑️ Amostra {id_amostra} removida.")