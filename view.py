import streamlit as st

def mostrar_titulo():
    st.title("Controle de Tarefas")

def mostrar_tarefas(tarefas):
    st.subheader("Tarefas Cadastradas")
    for t in tarefas:
        st.text(f"#{t[0]} - {t[1]}: {t[2]}")

def mostrar_formulario():
    st.subheader("Adicionar Nova Tarefa")
    with st.form(key="nova_tarefa"):
        titulo = st.text_input("Título")
        descricao = st.text_area("Descrição")
        enviar = st.form_submit_button("Adicionar")
    return titulo, descricao, enviar

def mostrar_exclusao():
    return st.number_input("ID da tarefa para deletar", min_value=1, step=1), st.button("Excluir")
