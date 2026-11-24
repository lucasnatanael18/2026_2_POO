import streamlit as st
from service import Service


class ManterClienteUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de clientes")
        operacao = st.radio(
            "Operação",
            ["Listar", "Inserir", "Atualizar", "Excluir"],
            horizontal=True,
            key="cliente_operacao",
        )

        if operacao == "Listar":
            ManterClienteUI.Listar()
        elif operacao == "Inserir":
            ManterClienteUI.Inserir()
        elif operacao == "Atualizar":
            ManterClienteUI.Atualizar()
        elif operacao == "Excluir":
            ManterClienteUI.Excluir()

    @staticmethod
    def Listar():
        clientes = Service.cliente_listar()
        st.subheader("Clientes cadastrados")
        if not clientes:
            st.info("Nenhum cliente cadastrado.")
            return

        st.dataframe(
            [
                {"ID": c.id, "Nome": c.nome, "E-mail": c.email, "Telefone": c.fone}
                for c in clientes
            ],
            use_container_width=True,
            hide_index=True,
        )

    @staticmethod
    def Inserir():
        st.subheader("Inserir cliente")
        with st.form("form_cliente_inserir", clear_on_submit=True):
            nome = st.text_input("Nome")
            email = st.text_input("E-mail")
            fone = st.text_input("Telefone")
            enviar = st.form_submit_button("Cadastrar cliente")

        if enviar:
            if not nome.strip() or not email.strip() or not fone.strip():
                st.error("Preencha todos os campos.")
                return
            Service.cliente_inserir(nome.strip(), email.strip(), fone.strip())
            st.success("Cliente cadastrado com sucesso.")

    @staticmethod
    def Atualizar():
        st.subheader("Atualizar cliente")
        clientes = Service.cliente_listar()
        if not clientes:
            st.info("Não há clientes para atualizar.")
            return

        opcoes = {f"{c.id} - {c.nome}": c.id for c in clientes}
        selecionado = st.selectbox("Selecione o cliente", list(opcoes), key="cliente_atualizar")
        cliente = Service.cliente_listar_id(opcoes[selecionado])
        if cliente is None:
            st.error("Cliente não encontrado.")
            return

        with st.form("form_cliente_atualizar"):
            nome = st.text_input("Nome", value=cliente.nome)
            email = st.text_input("E-mail", value=cliente.email)
            fone = st.text_input("Telefone", value=cliente.fone)
            enviar = st.form_submit_button("Salvar alterações")

        if enviar:
            if not nome.strip() or not email.strip() or not fone.strip():
                st.error("Preencha todos os campos.")
                return
            if Service.cliente_atualizar(cliente.id, nome.strip(), email.strip(), fone.strip()):
                st.success("Cliente atualizado com sucesso.")
            else:
                st.error("Não foi possível atualizar o cliente.")

    @staticmethod
    def Excluir():
        st.subheader("Excluir cliente")
        clientes = Service.cliente_listar()
        if not clientes:
            st.info("Não há clientes para excluir.")
            return

        opcoes = {f"{c.id} - {c.nome}": c.id for c in clientes}
        selecionado = st.selectbox("Selecione o cliente", list(opcoes), key="cliente_excluir")
        if st.button("Excluir cliente", type="primary"):
            if Service.cliente_excluir(opcoes[selecionado]):
                st.success("Cliente excluído com sucesso.")
                st.rerun()
            else:
                st.error("Cliente não encontrado.")
