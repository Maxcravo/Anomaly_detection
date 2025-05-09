import streamlit as st
from folium import folium, Marker 
from src.utils.bd_functions import bd_get_id
from src.utils.read_csv import read_image_csv
from streamlit_folium import st_folium  # type: ignore

st.title("This is the report page.")
st.write(st.session_state["report"])
if "report" not in st.session_state:
  st.error("Select a Report in saves page")
else:
  try:
    response = read_image_csv(st.session_state["report_date"], st.session_state["report"])
  except Exception as e:
    st.error("Error retrieving data from the database.")
    st.write(f"Error: {e}")
  if response_bd is None:
    st.error("Error in found data in BD")
  #TODO Transformar em função
  map =  folium.Map([float(response_bd[0].longitude), float(response_bd[0].latitude)], zoom_start=20)
  Marker(
    location=[float(response_bd[0].longitude), float(response_bd[0].latitude)],
    popup=f"location",
  ).add_to(map)
  
  st.markdown(f"#### the time of the report is **{response_bd[0].report_time}**")
  st.markdown(f"#### the date of the report is {response_bd[0].report_day}")
  st.markdown(f"#### the latitude of the report is {response_bd[0].longitude}")
  st.markdown(f"#### the longitude of the report is {response_bd[0].latitude}")
  st_map = st_folium(map, width=900)