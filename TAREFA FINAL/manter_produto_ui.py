import streamlit as st
from service import Service


class ManterProdutoUI:
    @staticmethod
    def Main():
        st.title("Manter cadastro de produtos")
        operacao = st.radio(
            "Operação",
            ["Listar", "Inserir", "Atualizar", "Excluir"],
            horizontal=True,
            key="produto_operacao",
        )

        if operacao == "Listar":
            ManterProdutoUI.Listar()
        elif operacao == "Inserir":
            ManterProdutoUI.Inserir()
        elif operacao == "Atualizar":
            ManterProdutoUI.Atualizar()
        elif operacao == "Excluir":
            ManterProdutoUI.Excluir()

    @staticmethod
    def Listar():
        produtos = Service.produto_listar()
        st.subheader("Produtos cadastrados")
        if not produtos:
            st.info("Nenhum produto cadastrado.")
            return

        linhas = []
        for produto in produtos:
            categoria = Service.categoria_listar_id(produto.id_categoria)
            linhas.append({
                "ID": produto.id,
                "Descrição": produto.descricao,
                "Preço": f"R$ {produto.preco:.2f}",
                "Estoque": produto.estoque,
                "Categoria": categoria.descricao if categoria else "Categoria não encontrada",
            })
        st.dataframe(linhas, use_container_width=True, hide_index=True)

    @staticmethod
    def Inserir():
        st.subheader("Inserir produto")
        categorias = Service.categoria_listar()
        if not categorias:
            st.warning("Cadastre uma categoria antes de cadastrar produtos.")
            return

        opcoes = {f"{c.id} - {c.descricao}": c.id for c in categorias}
        with st.form("form_produto_inserir", clear_on_submit=True):
            descricao = st.text_input("Descrição")
            preco = st.number_input("Preço (R$)", min_value=0.0, step=0.50, format="%.2f")
            estoque = st.number_input("Quantidade em estoque", min_value=0, step=1)
            categoria = st.selectbox("Categoria", list(opcoes))
            enviar = st.form_submit_button("Cadastrar produto")

        if enviar:
            if not descricao.strip():
                st.error("Informe a descrição do produto.")
                return
            resultado = Service.produto_inserir(
                descricao.strip(), float(preco), int(estoque), opcoes[categoria]
            )
            if resultado:
                st.success("Produto cadastrado com sucesso.")
            else:
                st.error("Não foi possível cadastrar o produto. Confira os dados.")

    @staticmethod
    def Atualizar():
        st.subheader("Atualizar produto")
        produtos = Service.produto_listar()
        categorias = Service.categoria_listar()
        if not produtos:
            st.info("Não há produtos para atualizar.")
            return
        if not categorias:
            st.warning("Cadastre uma categoria antes de atualizar produtos.")
            return

        opcoes_produtos = {f"{p.id} - {p.descricao}": p.id for p in produtos}
        selecionado = st.selectbox(
            "Selecione o produto", list(opcoes_produtos), key="produto_atualizar"
        )
        produto = Service.produto_listar_id(opcoes_produtos[selecionado])
        if produto is None:
            st.error("Produto não encontrado.")
            return

        opcoes_categorias = {f"{c.id} - {c.descricao}": c.id for c in categorias}
        rotulo_categoria_atual = next(
            (rotulo for rotulo, cid in opcoes_categorias.items()
             if cid == produto.id_categoria),
            list(opcoes_categorias)[0],
        )

        with st.form("form_produto_atualizar"):
            descricao = st.text_input("Descrição", value=produto.descricao)
            preco = st.number_input(
                "Preço (R$)", min_value=0.0, value=float(produto.preco),
                step=0.50, format="%.2f"
            )
            estoque = st.number_input(
                "Quantidade em estoque", min_value=0, value=int(produto.estoque), step=1
            )
            categoria = st.selectbox(
                "Categoria",
                list(opcoes_categorias),
                index=list(opcoes_categorias).index(rotulo_categoria_atual),
            )
            enviar = st.form_submit_button("Salvar alterações")

        if enviar:
            if not descricao.strip():
                st.error("Informe a descrição do produto.")
                return
            resultado = Service.produto_atualizar(
                produto.id, descricao.strip(), float(preco), int(estoque),
                opcoes_categorias[categoria]
            )
            if resultado:
                st.success("Produto atualizado com sucesso.")
            else:
                st.error("Não foi possível atualizar o produto. Confira os dados.")

    @staticmethod
    def Excluir():
        st.subheader("Excluir produto")
        produtos = Service.produto_listar()
        if not produtos:
            st.info("Não há produtos para excluir.")
            return

        opcoes = {f"{p.id} - {p.descricao}": p.id for p in produtos}
        selecionado = st.selectbox("Selecione o produto", list(opcoes), key="produto_excluir")
        if st.button("Excluir produto", type="primary"):
            if Service.produto_excluir(opcoes[selecionado]):
                st.success("Produto excluído com sucesso.")
                st.rerun()
            else:
                st.error("Produto não encontrado.")
