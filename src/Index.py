import sys, os, time 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
import streamlit as st
from src.utils.model_init import violence_model, gun_model
from src.utils.image_compress import compress_img
import dotenv
dotenv.load_dotenv()

if "compressed_frame" not in st.session_state:
  st.session_state.compressed_frame = []

st.title("Camera Stream")
# Input for the camera stream URL
camera_url = st.text_input(
    label="Enter the camera stream URL",
    key="camera_stream_url",
    placeholder="http:// or rtsp://"
)
# Initialize the models
model_violence = violence_model()
model_gun = gun_model()
names = model_violence.names
# Button to start the stream
start_stream = st.button("Start Stream")

#TODO Transformar em uma função e colocar no src/utils
# if start_stream and camera_url:
if start_stream:
  # cap = cv2.VideoCapture(camera_url)
  #! Test videoCap notebook
  cap = cv2.VideoCapture(0)
  
  fps = cap.get(cv2.CAP_PROP_FPS)
  frame_skip = int(fps / 3) 
  frame_count = 0 
  if not cap.isOpened():
      st.error("Error: Unable to open video stream. Please check the URL.")
  else:
    stop_stream = st.button("Stop Stream")
    # Stream frames to the Streamlit app
    while cap.isOpened() and not stop_stream:
      if frame_count % frame_skip == 0:
        ret, frame = cap.read()
        result_violence = model_violence.predict(frame, conf=0.85)
        result_gun = model_gun.predict(frame, conf=0.60)
        if len(result_violence[0].boxes) > 0:
          loop_time:float = time.time() + 5 # Temos que começar a contagem apenas depois que o primeiro frame de violência for detectado
          st.write("Violence outside the loop")
          while time.time() < loop_time:
            #! Dentro desse loop temos que ler os frames chamando mais uma vez o cap.read()
            ret_loop, frame_loop = cap.read()
            if frame_count % frame_skip == 0:
              if not ret_loop:
                st.error("error")
                break
              st.image(frame_loop, channels="RGB")
              st.session_state.compressed_frame.append(compress_img(frame_loop))
        if not ret:
          st.error("Error: Unable to read frame from stream.")
          break
        #Debug Display the frame in the Streamlit app
    # Release resources
    cap.release()
    st.success("Stream stopped.")

button_decode = st.button("see image compressed")
if button_decode:
  for frame in st.session_state.compressed_frame:
    decode_frame = cv2.imdecode(frame,1)
    st.image(decode_frame, channels="RGB")