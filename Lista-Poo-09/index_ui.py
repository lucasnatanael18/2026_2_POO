import streamlit as st

from manter_cliente_ui import ManterClienteUI
from manter_categoria_ui import ManterCategoriaUI
from manter_produto_ui import ManterProdutoUI
from reajustar_produto_ui import ReajustarProdutoUI


class IndexUI:
    @staticmethod
    def Main():
        """Apresenta o menu principal e direciona para a página escolhida."""
        pagina = st.sidebar.selectbox(
            "Selecione a página",
            [
                "Início",
                "Manter cadastro de clientes",
                "Manter cadastro de categorias",
                "Manter cadastro de produtos",
                "Reajustar preço de produtos",
            ],
        )

        if pagina == "Início":
            IndexUI.Inicio()
        elif pagina == "Manter cadastro de clientes":
            ManterClienteUI.Main()
        elif pagina == "Manter cadastro de categorias":
            ManterCategoriaUI.Main()
        elif pagina == "Manter cadastro de produtos":
            ManterProdutoUI.Main()
        elif pagina == "Reajustar preço de produtos":
            ReajustarProdutoUI.Main()

    @staticmethod
    def Inicio():
        """Página inicial do sistema."""
        from service import Service

        st.title("Sistema de Comércio Eletrônico")
        st.write("Selecione uma opção no menu lateral para começar.")

        clientes = Service.cliente_listar()
        categorias = Service.categoria_listar()
        produtos = Service.produto_listar()

        col1, col2, col3 = st.columns(3)
        col1.metric("Clientes cadastrados", len(clientes))
        col2.metric("Categorias cadastradas", len(categorias))
        col3.metric("Produtos cadastrados", len(produtos))
