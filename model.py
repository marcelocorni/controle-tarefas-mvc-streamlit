import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="tarefas",
        user="postgres",
        password="postgres",
        host="db",
        port="5432"
    )

def listar_tarefas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, titulo, descricao FROM tarefas ORDER BY id")
    tarefas = cur.fetchall()
    cur.close()
    conn.close()
    return tarefas

def adicionar_tarefa(titulo, descricao):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)", (titulo, descricao))
    conn.commit()
    cur.close()
    conn.close()

def deletar_tarefa(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tarefas WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
