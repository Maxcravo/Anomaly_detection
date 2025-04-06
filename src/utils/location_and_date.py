from datetime import date, datetime
from dotenv import load_dotenv
import os
load_dotenv()


def location() -> tuple:
  longitude = os.getenv("LONGITUDE")
  latitude = os.getenv("LATITUDE")
  return (longitude, latitude)


def time_date() -> str:
  day: str = str(date.today())
  time = datetime.now().strftime("%H:%M:%S")
  return (f"{day} - {time}")
  