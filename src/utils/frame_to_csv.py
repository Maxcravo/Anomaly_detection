import pandas as pd
import base64
from datetime import date
import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path = os.path.join(dir, "data/csv")


#* Aqui é importante pontuar que inserir a imagem no formato NDARRAY é impossível em um DATAFRAME
#* Assim acesso as informações da imagem na lista e codifico ela no formato base64
def frame_to_csv(compressed_frame:list):
  frame_data = []
  try:
    for element in compressed_frame:
      for frame in element:
        img_to_base64:str = base64.b64encode(frame).decode("utf-8")
        frame_data.append({"date": str(date.today()), "image": img_to_base64})
    print("i am here")
    df = pd.DataFrame(frame_data)
    df.to_csv(f"{path}/{str(date.today())}.csv", index=False)
  except Exception as e:
    print(e)
  
