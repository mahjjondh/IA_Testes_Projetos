import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
import pages as pg

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Sumarizador","Q&A","Ajuda"]
parent_dir = os.path.dirname(os.path.abspath(__file__))
#logo_path = os.path.join(parent_dir, "imagem.png")
#urls = {"Ajuda": "https://www.google.com"}
styles = {
    "nav": {
        "background-color": "#4377B6",
    },
    "img": {
        "padding-right": "10px",
    },
    "span": {
        "color": "white",
        "padding": "12px",
    },
    "active": {
        "color": "var(--text-color)",
        "background-color": "white",
        "font-weight": "normal",
        "padding": "12px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

page = st_navbar(
    pages,
#    logo_path=logo_path,
#    urls=urls,
    styles=styles,
    options=options,
)

functions = {
    "Sumarizador": pg.show_sumarizador,
    "Q&A": pg.show_qa,
    "Ajuda": pg.show_help,
    }
go_to = functions.get(page)
if go_to:
    go_to()
