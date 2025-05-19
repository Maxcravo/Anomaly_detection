import streamlit as st
from folium import folium, Marker 
from src.utils.bd_functions import bd_get_id
from src.utils.read_csv import read_image_csv, csv_lat_long
from streamlit_folium import st_folium  # type: ignore

st.title("This is the report page.")
st.write(st.session_state["report_date"])
st.write(st.session_state["report"])
if st.session_state["report_date"] is None:
  st.error("Select a report in saves page")
  
try:
  response = read_image_csv(st.session_state["report_date"], st.session_state["report"])
  lat_long = csv_lat_long(st.session_state["report_date"])
  if response is None or lat_long is None:
    st.error("error in get the images")
    st.stop()
except Exception as e:
  st.error(f"Error in read image {e}")
  st.stop()  
for image in response:
  st.image(response)
map =  folium.Map([float(lat_long[1]), float(lat_long[0])], zoom_start=20)
Marker(
  location= [float(lat_long[1]), float(lat_long[0])],
  popup=f"location",
).add_to(map)



st.markdown(f"#### the time of the report is **{st.session_state["report"]}**")
st.markdown(f"#### the date of the report is {st.session_state["report_date"]}")
# st.markdown(f"#### the latitude of the report is {response_bd[0].longitude}")
# st.markdown(f"#### the longitude of the report is {response_bd[0].latitude}")
st_map = st_folium(map, width=900)