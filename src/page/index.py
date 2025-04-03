import sys
import os
import cv2
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from src.utils.model_init import violence_model, gun_model


st.title("Camera Stream")
# Input for the camera stream URL
camera_url = st.text_input(
    label="Enter the camera stream URL",
    key="camera_stream_url",
    placeholder="http:// or rtsp://"
)
model_violence = violence_model()
model_gun = gun_model()
# Button to start the stream
start_stream = st.button("Start Stream")

#TODO Transformar em uma função e colocar no src/utils
if start_stream and camera_url:
    cap = cv2.VideoCapture(camera_url)
    if not cap.isOpened():
        st.error("Error: Unable to open video stream. Please check the URL.")
    else:
        stop_stream = st.button("Stop Stream")
        # Stream frames to the Streamlit app
        while cap.isOpened() and not stop_stream:
            # st.write("Streaming...")
            ret, frame = cap.read()
            result_violence = model_violence.predict(frame, conf=0.70)
            result_gun = model_gun.predict(frame, conf=0.60)
            if not ret:
                st.error("Error: Unable to read frame from stream.")
                st.write("The video stream is stopped")
                break
            # Display the frame in the Streamlit app
            # st.image(frame, channels="BGR")

        # Release resources
        cap.release()
        st.success("Stream stopped.")