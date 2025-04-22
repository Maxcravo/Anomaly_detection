import streamlit as st
from src.utils.bd_functions import bd_get
from src.utils.read_csv import read_csv

if "report" not in st.session_state:
  st.session_state.report = None
# Para cada elemento que eu tiver salvo eu tenho que recuperar os saves e adicionar aqui na página
# O jeito que encontrei foi criar uma página para cada save, posso fazer isso dinamicamente criando um arquivo temporário para cada save que recuperei do banco de dados.
search_report = st.text_input(label="enter the date of the save", placeholder="year-mounth-day" )
search_button = st.button(label="search")

try:
  assert len(search_report) == 10 and search_report[4] == "-" and search_report[7] == "-"
  if search_report and search_button:
    result = read_csv(search_report)
  if result == None:
    st.error("No data found for the given date.")
  else:
    st.success("Data retrieved successfully.")
    col1, col2, col3 = st.columns(3)
    with col1:
      for result in result:
        if st.page_link(page="pages/report.py", label=f"{result[1]}"):
          st.session_state.report = result[0]
except AssertionError:
  st.error("Invalid date format. Please use YYYY-MM-DD.")
#TODO tratar o erro caso o retorno da função não seja um dataframe (é necessário?)
except ValueError:
  pass

    