import pandas as pd
import base64
from datetime import date, datetime
import os
import streamlit as st
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
path = os.path.join(dir, "data/reports")


#* Aqui é importante pontuar que inserir a imagem no formato NDARRAY é impossível em um DATAFRAME
#* Assim acesso as informações da imagem na lista e codifico ela no formato base64
def frame_to_csv(compressed_frame:list):
  frame_data = []
  try:
    for element in compressed_frame:
      for frame in element:
        img_to_base64:str = base64.b64encode(frame).decode("utf-8")
        #* Aqui estamos pegando a data e o horário em que está sendo capturado o frame juntamente com os dados codificados do frame em si, todos os frames salvos naquela identificação de violência em específico serão salvos com o mesmo horário, de modo que usaremos esse valor para identificar cada ocorrência.
        frame_data.append({"date": str(date.today()), "image": img_to_base64, "time": str(datetime.now().strftime("%H:%M:%S")), "latitude": st.session_state.latitude_longitude.get("latitude") , "longitude": st.session_state.latitude_longitude.get("longitude") }) 
    df = pd.DataFrame(frame_data)
    if os.path.exists(f"{path}/{str(date.today())}.csv") == False: #* Caso o arquivo não exista, criamos um novo com o header
      df.to_csv(f"{path}/{str(date.today())}.csv", index=False) 
    if os.path.exists(f"{path}/{str(date.today())}.csv")== True:
      df.to_csv(f"{path}/{str(date.today())}.csv", index=False, header=False, mode="a") #* caso o arquivo já exista, apenas adicionamos os novos frames ao fim do arquivo
  except Exception as e:
    print(e)
  
