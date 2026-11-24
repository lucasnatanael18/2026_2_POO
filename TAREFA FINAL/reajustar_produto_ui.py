import streamlit as st
from service import Service


class ReajustarProdutoUI:
    @staticmethod
    def Main():
        st.title("Reajustar preço dos produtos")
        ReajustarProdutoUI.Reajustar()

    @staticmethod
    def Reajustar():
        produtos = Service.produto_listar()
        if not produtos:
            st.info("Não há produtos cadastrados para reajustar.")
            return

        st.dataframe(
            [
                {
                    "ID": p.id,
                    "Descrição": p.descricao,
                    "Preço atual": f"R$ {p.preco:.2f}",
                }
                for p in produtos
            ],
            use_container_width=True,
            hide_index=True,
        )

        with st.form("form_reajustar_produtos"):
            percentual = st.number_input(
                "Percentual de reajuste (%)",
                value=0.0,
                step=1.0,
                format="%.2f",
                help="Use percentual positivo para aumentar e negativo para reduzir os preços.",
            )
            enviar = st.form_submit_button("Aplicar reajuste")

        if enviar:
            if percentual <= -100:
                st.error("O percentual não pode ser igual ou inferior a -100%.")
                return
            try:
                Service.produto_reajustar(float(percentual))
                st.success(f"Reajuste de {percentual:.2f}% aplicado com sucesso.")
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
