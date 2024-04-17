import streamlit as st


def show_help():
    st.header("Ajuda")
    st.write(
        """
        Este aplicativo tem finalidade em ajudar a compreensão de processos da justiça.
        Ele utiliza modelos de IA para sumarizar e extrair informações de documentos.
        Este aplicativo não substitui a análise de um profissional da área jurídica,
        e tem como objetivo auxiliar na compreensão de documentos e na aumentar a eficiencia no 
        uso de tempo e processo de analise de documentos.

        Modelos Utilizados:
        - Sumarização de Texto
        - Extração de Informações
        """
    )
