from ultralytics import YOLO
import os

def violence_model():
  """Return the yolo model that recognize violence in a frame"""
  dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
  model_path = os.path.join(dir, "data", "yolo11s_violence_detection.pt" )
  model = YOLO(model_path)  
  model.sett
  return model