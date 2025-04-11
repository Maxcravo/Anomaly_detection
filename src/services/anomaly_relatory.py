from src.utils.location_and_date import location, time_date
import os

def anomaly_report() -> None:
    """Aqui retornamos um novo arquivo de relatório"""
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(dir, "data/reports")
    longitude, latitude = location()
    day = time_date()
    
    with open(f"{path}/report_{day}.txt", "w") as file:
      file.write(f"O dia e horário em que ocorreu a situação foi {day} \n")
      file.write(f"The local of the anomaly is latidude:{latitude} longitude: {longitude} \n")
      
      
    