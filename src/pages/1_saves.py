import streamlit as st

# Para cada elemento que eu tiver salvo eu tenho que recuperar os saves e adicionar aqui na página
# O jeito que encontrei foi criar uma página para cada save, posso fazer isso dinamicamente criando um arquivo temporário para cada save que recuperei do banco de dados.
st.text_input(label="enter the date of the save")

col1, col2, col3 = st.columns(3)

with col1:
  st.page_link(label="save 1", page="Index.py")
  
with col2:
  st.page_link(label="save 1", page="Index.py")
  
with col3:
  st.page_link(label="save 1", page="Index.py")