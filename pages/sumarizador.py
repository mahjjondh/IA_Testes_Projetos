import streamlit as st
import fitz
from huggingface_hub import InferenceClient

def show_sumarizador():
    token = st.text_input('Insira seu Token do HF', type='password')
    headers = {'Authorization': f'Bearer {token}'}
    client = InferenceClient("sshleifer/distilbart-cnn-12-6", headers=headers)
    st.title('Sumarizador de Texto')
    st.write('Utilize o campo abaixo para fazer upload do arquivo PDF que deseja sumarizar.')
    uploaded_file = st.file_uploader("Escolha o arquivo PDF", type="pdf")
    if uploaded_file is not None:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype='pdf')
        text = ''
        for page in pdf_document:
            text += page.get_text()
        st.write("Texto Resumido:")
        sumario = client.summarization(text)
        st.write(sumario['summary_text'])

