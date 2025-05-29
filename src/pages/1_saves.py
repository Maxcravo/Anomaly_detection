import streamlit as st
from src.utils.bd_functions import bd_get
from src.utils.read_csv import csv_time

# Para cada elemento que eu tiver salvo eu tenho que recuperar os saves e adicionar aqui na página
# O jeito que encontrei foi criar uma página para cada save, posso fazer isso dinamicamente criando um arquivo temporário para cada save que recuperei do banco de dados.
search_report = st.text_input(label="enter the date of the save", placeholder="year-mounth-day" )
search_button = st.button(label="search")

def button_clicked(date, time):
  st.session_state.report_date = date
  st.session_state.report = time

try:
  buttons = []
  assert len(search_report) == 10 and search_report[4] == "-" and search_report[7] == "-"
  if search_report and search_button:
    #TODO Agora preciso pegar o arquivo que foi salvo, e associa aquela data pegar todos os diferentes horarios que foram obtidos
    #! Não consigui fazer o redirect para a página de report diretamente.
    nbuttons = csv_time(search_report)
    if nbuttons is None:
      st.warning("error in read the csv")
      st.stop()
    cols = st.columns(5)
    st.warning("Select the time of the report and go to report page")
    for n, button in enumerate(nbuttons):
      with cols[n]:
          st.button(f"{button}", on_click=button_clicked, kwargs={"date": search_report, "time": button})
  st.page_link(page="pages/report.py", label="report page")
  
except AssertionError:
  st.error("Invalid date format. Please use YYYY-MM-DD.")
#TODO tratar o erro caso o retorno da função não seja um dataframe (é necessário?)
except ValueError:
  pass

    