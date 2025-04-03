from ultralytics import YOLO
import os

def violence_model():
  """Return the yolo model that recognize violence in a frame"""
  dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
  model_path = os.path.join(dir, "data", "yolo11s_violence_detection.pt" )
  model = YOLO(model_path) 
  return model

#https://huggingface.co/wuhp/guns-100-11m/commit/e6b2d0d20fce98d904ae00f40b1581ad1a67bcb2
def gun_model():
  """Return the yolo model that recognize gun and knife in a frame"""
  dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
  model_path = os.path.join(dir, "data", "Guns-100-11m.pt" )
  model = YOLO(model_path) 
  print(model.names)
  return model
