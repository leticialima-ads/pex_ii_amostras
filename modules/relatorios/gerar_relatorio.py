import sqlite3

def relatorio_geral():
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM amostras")
    total_amostras = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM pesquisadores")
    total_pesquisadores = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM resultados WHERE status='Concluído'")
    concluidos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM resultados WHERE status='Em análise'")
    em_analise = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM resultados WHERE status='Inválido'")
    invalidos = cursor.fetchone()[0]

    conexao.close()

    print(f"📋 Total de amostras: {total_amostras}")
    print(f"👩‍🔬 Pesquisadores registrados: {total_pesquisadores}")
    print(f"✅ Concluídas: {concluidos}")
    print(f"🔬 Em análise: {em_analise}")
    print(f"⚠️ Inválidas: {invalidos}")