
# 📋 Controle de Tarefas com Streamlit (MVC) + PostgreSQL + Docker

Este projeto demonstra como aplicar a arquitetura **MVC (Model-View-Controller)** em Python utilizando o framework **Streamlit**, com persistência de dados em um banco **PostgreSQL**, totalmente orquestrado com **Docker**.

---

## 🎯 Objetivos

- Demonstrar a aplicação prática do padrão **MVC** usando Streamlit
- Ensinar como estruturar uma aplicação modular e didática
- Realizar operações de **CRUD de tarefas** (Criar, Listar, Excluir)
- Integrar a aplicação a um banco de dados PostgreSQL
- Orquestrar a aplicação completa usando Docker e Docker Compose

---

## 🧱 Estrutura do Projeto

```
controle_tarefas/
├── app.py                  # Entrada principal da aplicação Streamlit
├── controller.py           # Lógica de controle (Controller)
├── model.py                # Acesso ao banco de dados (Model)
├── view.py                 # Interface visual com o usuário (View)
├── Dockerfile              # Imagem do app Streamlit
├── docker-compose.yml      # Orquestração dos containers
├── requirements.txt        # Dependências Python
└── db/
    └── init.sql            # Script de criação da tabela tarefas
```

---

## 🚀 Como Executar o Projeto

### 🔧 Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### ▶️ Passos

1. Clone o repositório:

```bash
git clone https://github.com/marcelo.corni/controle-tarefas-mvc-streamlit.git
cd controle-tarefas-mvc-streamlit
```

2. Inicie os containers:

```bash
docker-compose up --build
```

3. Acesse no navegador:

```
http://localhost:8501
```

---

## 🗄️ Acesso ao Banco via DBeaver (opcional)

Você pode conectar ao PostgreSQL usando ferramentas como **DBeaver**:

- **Host:** `localhost`
- **Porta:** `5433`
- **Usuário:** `postgres`
- **Senha:** `postgres`
- **Banco:** `tarefas`

---

## ⚙️ Funcionalidades da Aplicação

- ✅ Listar todas as tarefas registradas
- ➕ Adicionar nova tarefa com título e descrição
- ❌ Excluir tarefas por ID

---

## 📌 Tecnologias Utilizadas

- **Python 3.11**
- **Streamlit**
- **PostgreSQL 15**
- **Docker e Docker Compose**
- **psycopg2-binary** (driver PostgreSQL)

---

## 🎓 Ideal para:

- Estudantes de Python
- Quem deseja entender MVC na prática
- Professores e tutores que ensinam desenvolvimento web com dados

---

## ✍️ Autor

Desenvolvido por Marcelo Corni Alves
Se curtiu, ⭐️ dê uma estrela no repositório!
