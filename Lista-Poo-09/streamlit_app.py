import streamlit as st
from index_ui import IndexUI


def main():
    st.set_page_config(
        page_title="Sistema de Comércio Eletrônico",
        page_icon="🛒",
        layout="wide",
    )
    IndexUI.Main()


if __name__ == "__main__":
    main()
