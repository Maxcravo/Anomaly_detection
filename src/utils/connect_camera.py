import cv2
from aiortc.contrib.media import MediaPlayer
from aiortc.contrib.media import MediaRecorder
from streamlit_webrtc import webrtc_streamer
import streamlit as st

#"http://10.0.0.122:4747/video"

webrtc = webrtc_streamer(
   key="test",
   video_processor_factory=None,
   rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
   media_stream_constraints={
       "video": True,
       "audio": False
   },
)

def capture(capture_stream_url):
  """ Reminder that the video stream or is http or rtsp"""
  if webrtc.video_receiver:
    capture_stream = cv2.VideoCapture(capture_stream_url)
    if not capture_stream.isOpened():
          print("Error: Unable to open video stream.")
          return
    while True:
      ret, frame = capture_stream.read()
      print(f"Frame shape: {frame.shape}")
      if ret:
         webrtc.video_receiver.process_frame(frame)
         return frame
        #  st.image(frame, channels="BGR")
      try:
        cv2.imshow("frame", cv2.resize(frame, (640, 480)))
        key = cv2.waitKey(1)
        if key == ord('q'):
          break
      except cv2.error as e:
        print(f"Error in capture Stream {e}")
        break
    capture_stream.release()
    cv2.destroyAllWindows()

