import streamlit as st
from sqlalchemy.sql import text

def bd_insert(date:str, time:str, latitude:str, longitude:str):
  conn = st.connection("mysql")
  with conn.session as s:
    try:
    # Acesso o horario e o dia em que aconteceu a ocorrência
      s.execute(text(f"INSERT INTO anomaly_report (report_day, report_time, longitude, latitude) VALUES ('{date}', '{time}', '{latitude}', '{longitude}')"))
      s.commit()
      st.success("Data inserted successfully.")
    except Exception as e:
      print(f"Error inserting data: {e}")
      s.rollback()
      return st.error("Error insert data in the database.")

def bd_get(search_date:str) -> list:
  try:
    conn = st.connection("mysql")
    with conn.session as s:
      result = s.execute(text(f"SELECT ID, report_day FROM anomaly_report WHERE report_day = '{search_date}'"))
      return list(result.fetchall())
  except Exception as e:
    print(f"Error retrieving data: {e}")
    return st.error("Error retrieving data from the database.")
  
def bd_get_id(id:int) -> list:
  try:
    conn = st.connection("mysql")
    with conn.session as s:
      result = s.execute(text(f"SELECT * FROM anomaly_report WHERE ID = {id}"))
      return list(result.fetchall())
  except Exception as e:
    print(f"Error retrieving data: {e}")
    return st.error("Error retrieving data from the database.")