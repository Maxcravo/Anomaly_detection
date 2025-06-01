import streamlit as st
from folium import folium, Marker 
from src.utils.bd_functions import bd_get_id
from src.utils.read_csv import read_image_csv, csv_lat_long
from streamlit_folium import st_folium  # type: ignore
from src.utils.remove_report import remove_report
from PIL import Image

st.title("This is the report page.")

if st.session_state["report_date"] is None:
  st.error("Select a report in saves page")
if "counter" not in st.session_state:
  st.session_state["counter"] = 0
st.markdown(f"#### the time of the report is **{st.session_state["report"]}**")
st.markdown(f"#### the date of the report is {st.session_state["report_date"]}")

try:
  response = read_image_csv(st.session_state["report_date"], st.session_state["report"])
  lat_long = csv_lat_long(st.session_state["report_date"])
  if response is None or lat_long is None:
    st.error("error in get the images")
    st.stop()
except Exception as e:
  st.error(f"Error in read image {e}")
  st.stop()  
  
# CREDIT: https://discuss.streamlit.io/t/display-images-one-by-one-with-a-next-button/21976/3
def showReport(report_image):
  col2.image(report_image, caption="report image")
  st.session_state["counter"] += 1
  if st.session_state["counter"] >= len(response): # type: ignore
    st.session_state["counter"] = 0
  

col1,col2 = st.columns(2)
col1.text("O REPORT É VERIDICO?")

photo = response[st.session_state["counter"]]
btn = col1.button("next report image", on_click=showReport, args=(photo,))
col1.button("sim")
col1.button("não", on_click=remove_report, kwargs={"date": st.session_state["report_date"], "time": st.session_state["report"]})

map =  folium.Map([float(lat_long[1]), float(lat_long[0])], zoom_start=20)
Marker(
  location= [float(lat_long[1]), float(lat_long[0])],
  popup=f"location",
).add_to(map)
# st.markdown(f"#### the latitude of the report is {response_bd[0].longitude}")
# st.markdown(f"#### the longitude of the report is {response_bd[0].latitude}")
st_map = st_folium(map, width=900)