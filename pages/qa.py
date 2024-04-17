import streamlit as st 
import fitz
from huggingface_hub import InferenceClient

#client = InferenceClient("pierreguillou/bert-base-cased-squad-v1.1-portuguese")
#client.question_answering()
#client = InferenceClient()




def show_qa():
    token = st.text_input("Use o seu token do Hugging Face", type="password")
    headers = {"Authorization": f"Bearer {token}"}
    client = InferenceClient("pierreguillou/bert-base-cased-squad-v1.1-portuguese", headers=headers)
    st.title('Responda Questões sobre o PDF')
    st.write('Aqui você pode responder questões sobre o PDF que você fez upload')
    st.write('Para isso, basta clicar no botão abaixo e selecionar o arquivo PDF que deseja responder as questões')
    uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ''
        for page in doc:
            text += page.get_text()
        st.write("Use o campo abaixo para fazer perguntas sobre o PDF")
        #question = st.text_input('Pergunta')
        messages = st.container(height=300)
        #chat = []
        if prompt := st.chat_input("Say something"):
            messages.chat_message("user").write(prompt)
            qa = client.question_answering(context=text, question=str(prompt))
            messages.chat_message("assistant").write(f"Bot: {qa['answer'], round((qa['score']*100),2)}%")


