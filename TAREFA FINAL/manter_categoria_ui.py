import streamlit as st
from service import Service


class ManterCategoriaUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de categorias")
        operacao = st.radio(
            "Operação",
            ["Listar", "Inserir", "Atualizar", "Excluir"],
            horizontal=True,
            key="categoria_operacao",
        )

        if operacao == "Listar":
            ManterCategoriaUI.Listar()
        elif operacao == "Inserir":
            ManterCategoriaUI.Inserir()
        elif operacao == "Atualizar":
            ManterCategoriaUI.Atualizar()
        elif operacao == "Excluir":
            ManterCategoriaUI.Excluir()

    @staticmethod
    def Listar():
        categorias = Service.categoria_listar()
        st.subheader("Categorias cadastradas")
        if not categorias:
            st.info("Nenhuma categoria cadastrada.")
            return
        st.dataframe(
            [{"ID": c.id, "Descrição": c.descricao} for c in categorias],
            use_container_width=True,
            hide_index=True,
        )

    @staticmethod
    def Inserir():
        st.subheader("Inserir categoria")
        with st.form("form_categoria_inserir", clear_on_submit=True):
            descricao = st.text_input("Descrição")
            enviar = st.form_submit_button("Cadastrar categoria")

        if enviar:
            if not descricao.strip():
                st.error("Informe a descrição da categoria.")
                return
            Service.categoria_inserir(descricao.strip())
            st.success("Categoria cadastrada com sucesso.")

    @staticmethod
    def Atualizar():
        st.subheader("Atualizar categoria")
        categorias = Service.categoria_listar()
        if not categorias:
            st.info("Não há categorias para atualizar.")
            return

        opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
        selecionado = st.selectbox("Selecione a categoria", list(opcoes), key="categoria_atualizar")
        categoria = Service.categoria_listar_id(opcoes[selecionado])
        if categoria is None:
            st.error("Categoria não encontrada.")
            return

        with st.form("form_categoria_atualizar"):
            descricao = st.text_input("Descrição", value=categoria.descricao)
            enviar = st.form_submit_button("Salvar alterações")

        if enviar:
            if not descricao.strip():
                st.error("Informe a descrição da categoria.")
                return
            if Service.categoria_atualizar(categoria.id, descricao.strip()):
                st.success("Categoria atualizada com sucesso.")
            else:
                st.error("Não foi possível atualizar a categoria.")

    @staticmethod
    def Excluir():
        st.subheader("Excluir categoria")
        categorias = Service.categoria_listar()
        if not categorias:
            st.info("Não há categorias para excluir.")
            return

        opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
        selecionado = st.selectbox("Selecione a categoria", list(opcoes), key="categoria_excluir")
        categoria_id = opcoes[selecionado]

        # A Lista 07 permite excluir categorias mesmo quando há produtos associados.
        # A interface evita deixar produtos apontando para uma categoria inexistente.
        produtos_vinculados = [
            p for p in Service.produto_listar() if p.id_categoria == categoria_id
        ]
        if produtos_vinculados:
            st.warning(
                "Esta categoria não pode ser excluída porque existem produtos vinculados. "
                "Altere ou exclua esses produtos primeiro."
            )
            return

        if st.button("Excluir categoria", type="primary"):
            if Service.categoria_excluir(categoria_id):
                st.success("Categoria excluída com sucesso.")
                st.rerun()
            else:
                st.error("Categoria não encontrada.")
