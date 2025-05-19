import pandas as pd
import os
import base64
import numpy as np
import cv2
from cv2.typing import MatLike
from PIL import Image 
from src.utils.remove_duplicated import remove_duplicate

#TODO tenho que receber mais de um dataframe por data.
#! Não sei o porque mas o script está executando mais de uma vez. Não consigo resolver
def read_image_csv(date:str, time:str) -> list[MatLike]| None:
  print("read_image_csv Called")
  index = 0
  dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
  path = os.path.join(dir, "data/reports")
  img:list[MatLike] = []
  try:
    df = pd.read_csv(f"{path}/{date}.csv")
    image_column = df["image"]
  except FileNotFoundError as e:
    print(f"Error in read image '{e}'")
    return e # type: ignore
  for row in df.itertuples():
      time_value = getattr(row, "time")
      image_value = getattr(row, "image")
      index +=1
      print(time_value, index)
      if time_value == time:
        # base64 to bytes
        img_bytes = base64.b64decode(image_value)   # type: ignore
        # Bytes to np.unit8 array using numpy
        img_array = np.frombuffer(img_bytes, dtype=np.uint8)
        # use opencv to decode numpy array to matlike image
        img.append(cv2.imdecode(img_array, cv2.IMREAD_COLOR_RGB))
        if img is None:
          return f"error in image cv2 decode" # type: ignore
  if img is not None:
    img_unique = remove_duplicate(img)
    return img_unique

def csv_time(date:str) -> list| None:
  time_list = []
  try:
    df = pd.read_csv(f"./src/data/reports/{date}.csv")
  except FileNotFoundError as  e:
    print(f"Error in read csv {e}")
    return None
  for index, row in df.iterrows():
    time_list.append(row["time"])
  time_list_unique = list(set(time_list))
  if time_list is None:
    return None
  if time_list is not None:  
    print(time_list_unique)
    return time_list_unique
    
def csv_lat_long(date:str) -> list | None:
  lat_long = []
  try:
    df = pd.read_csv(f"./src/data/reports/{date}.csv")
  except FileNotFoundError as  e:
    print(f"Error in read csv {e}")
    return None
  lat_long.append(df.loc[0,"latitude"])
  lat_long.append(df.loc[0,"longitude"])
  if lat_long is None:
    return None
  if lat_long is not None:
    return lat_long
  


