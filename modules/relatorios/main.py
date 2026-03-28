import sqlite3
import os
from modules.pesquisadores import *
from modules.amostras import *
from modules.resultados import *
from relatorios.gerar_relatorio import relatorio_geral

# === Função de criação automática do banco ===
def criar_banco():
    conexao = sqlite3.connect("laboratorio.db")
    cursor = conexao.cursor()

    # Criação das tabelas, se não existirem
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pesquisadores (
        id_pesquisador INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especialidade TEXT,
        email TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS amostras (
        id_amostra INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_material TEXT NOT NULL,
        data_coleta TEXT NOT NULL,
        id_pesquisador INTEGER,
        FOREIGN KEY(id_pesquisador) REFERENCES pesquisadores(id_pesquisador)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resultados (
        id_resultado INTEGER PRIMARY KEY AUTOINCREMENT,
        id_amostra INTEGER,
        descricao TEXT,
        status TEXT,
        FOREIGN KEY(id_amostra) REFERENCES amostras(id_amostra)
    );
    """)

    conexao.commit()
    conexao.close()
    print("✅ Banco de dados criado ou verificado com sucesso!\n")


# === Execução principal ===
if __name__ == "__main__":
    # Cria o banco automaticamente se não existir
    if not os.path.exists("laboratorio.db"):
        criar_banco()
    else:
        print("Banco de dados já existente.\n")

    # Demonstração das funções
    adicionar_pesquisador("Dra. Helena Costa", "Genética Molecular", "helena@labbio.com")
    adicionar_pesquisador("Dr. Ismael Rocha", "Biotecnologia Celular", "ismael@labbio.com")

    adicionar_amostra("Sangue", "2025-11-08", 1)
    adicionar_amostra("Tecido", "2025-11-08", 2)

    adicionar_resultado(1, "Análise concluída com sucesso", "Concluído")
    adicionar_resultado(2, "Em andamento", "Em análise")

    print("\n=== PESQUISADORES ===")
    listar_pesquisadores()

    print("\n=== AMOSTRAS ===")
    listar_amostras()

    print("\n=== RESULTADOS ===")
    listar_resultados()

    print("\n=== RELATÓRIO GERAL ===")
    relatorio_geral()