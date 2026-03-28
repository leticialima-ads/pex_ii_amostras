# 🧪 Sistema de Gerenciamento de Laboratório

## 📌 Sobre o Projeto

Este projeto consiste em um sistema desenvolvido em Python para gerenciamento de dados laboratoriais, permitindo o controle de pesquisadores, amostras coletadas e resultados de análises.

A aplicação utiliza banco de dados SQLite para armazenamento persistente e foi estruturada de forma modular, facilitando manutenção, expansão e organização do código.

---

## 🎯 Objetivo

Simular e organizar o fluxo básico de um laboratório, permitindo:

* Cadastro de pesquisadores
* Registro de amostras
* Armazenamento de resultados
* Geração de relatórios

---

## 🚀 Funcionalidades

* 👩‍🔬 Cadastro de pesquisadores
* 🧫 Registro de amostras laboratoriais
* 📊 Inserção e consulta de resultados
* 📄 Geração de relatório geral
* 🗃️ Criação automática do banco de dados

---

## 🛠️ Tecnologias Utilizadas

* Python
* SQLite3
* Programação modular

---

## 🗄️ Estrutura do Banco de Dados

O sistema cria automaticamente o banco `laboratorio.db` com as seguintes tabelas:

* **pesquisadores**
* **amostras**
* **resultados**

Relacionamentos:

* Um pesquisador pode ter várias amostras
* Uma amostra pode ter um resultado associado

---

## 📂 Estrutura do Projeto

* `modules/` → Funções de manipulação de dados
* `relatorios/` → Geração de relatórios
* `main.py` → Execução principal do sistema

---

## 📌 Status do Projeto

✅ Funcional
🔧 Pode receber melhorias e novas funcionalidades

---

## 👩‍💻 Autora

Desenvolvido por **Letícia Lima** como projeto de estudo e prática em banco de dados e programação em Python.

---

## 📄 Licença

Projeto de uso acadêmico, livre para estudo e adaptação.
