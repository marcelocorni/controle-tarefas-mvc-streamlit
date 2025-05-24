import model
import view
import streamlit as st

def run():
    view.mostrar_titulo()

    titulo, descricao, enviar = view.mostrar_formulario()
    if enviar and titulo:
        model.adicionar_tarefa(titulo, descricao)
        st.success("Tarefa adicionada com sucesso!")

    tarefas = model.listar_tarefas()
    view.mostrar_tarefas(tarefas)

    id_excluir, excluir = view.mostrar_exclusao()
    if excluir:
        model.deletar_tarefa(int(id_excluir))        
        st.rerun()

        
