import sys, os, time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import streamlit as st
from src.utils.model_init import violence_model, gun_model
from src.utils.image_compress import compress_img
from src.utils.frame_to_csv import frame_to_csv
from src.services.face_blurry import face__blurry
import dotenv
dotenv.load_dotenv()

if "compressed_frame" not in st.session_state:
  st.session_state.compressed_frame = []

if "latitude_longitude" not in st.session_state:
  st.session_state.latitude_longitude = {"latitude": "", "longitude": ""}

st.title("Camera Stream")

latitude = st.text_input(
  label="Enter the latitude"
)
longitude = st.text_input(
  label="Enter the longitude"
)
# Input for the camera stream URL
camera_url = st.text_input(
    label="Enter the camera stream URL",
    key="camera_stream_url",
    placeholder="http:// or rtsp://"
)
# Initialize the models
names = violence_model().names
# Button to start the stream
start_stream = st.button("Start Stream")

# if start_stream and camera_url and longitude and latitude:
if start_stream and longitude and latitude:
  st.session_state.latitude_longitude.update(latitude = latitude, longitude = longitude)
  # cap = cv2.VideoCapture(camera_url)
  #! Test videoCap notebook
  cap = cv2.VideoCapture(0)
  #* set the camera to get 3 frames per second
  fps = cap.get(cv2.CAP_PROP_FPS)
  fps_out = 3
  index_in = -1
  index_out = -1

  if not cap.isOpened():
      st.error("Error: Unable to open video stream. Please check the URL.")
  else:
    stop_stream = st.button("Stop Stream")
    if stop_stream:
      cap.release()
    while cap.isOpened() and not stop_stream:
      cap_sucess = cap.grab()
      index_in +=1
      out = int(index_in/fps * fps_out)
      if out > index_out:
        cap_sucess, frame = cap.retrieve()
        index_out+=1
        result_violence = violence_model().predict(frame, conf=0.55) 
        #* Caso o modelo detecte violência, ele vai entrar no loop
        if len(result_violence[0].boxes) > 0: # type: ignore
          loop_time:float = time.time() + 5 #* Temos que começar a contagem apenas depois que o primeiro frame de violência for detectado, pegando os próximos 5 segundos\
          #* Dentro desse loop temos que ler os frames chamando mais uma vez o cap.retrieve()
          while time.time() < loop_time:
            cap_loop = cap.grab()
            index_in +=1
            out_loop = int(index_in/fps * fps_out)
            if out_loop > index_out:
              sucess_loop, frame_loop = cap.retrieve()
              index_out +=1
              frame_loop = face__blurry(frame_loop) #* Como foi identificado um frame de violência, aplicamos o blur no rosto dos envolvidos.
              st.image(frame_loop, channels="BGR")
              st.session_state.compressed_frame.append([compress_img(frame_loop)]) #* comprimimos a imagem e adicionamos na lista que está salva na sessão
              if not cap_sucess:
                st.error("error")
                break
        if not cap_sucess:
          st.error("Error: Unable to read frame from stream.")
          break
    # cap.release()
    st.success("Stream stopped.")

button_decode = st.button("create csv")
if button_decode:
  frame_to_csv(compressed_frame=st.session_state.compressed_frame)
  st.session_state.compressed_frame = []

  # for frame in st.session_state.compressed_frame:
  #   decode_frame = cv2.imdecode(frame,1)
  #   st.image(decode_frame, channels="RGB")
  