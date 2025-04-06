import streamlit as st
from sqlalchemy.sql import text

def bd_insert(anomaly_report:tuple):
  conn = st.connection("mysql")
  with conn.session as s:
    # Acesso o horario e o dia em que aconteceu a ocorrência
    s.execute(text(""))
    s.commit()