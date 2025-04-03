from datetime import date 
from dotenv import load_dotenv
import os
load_dotenv()


def location():
  longitude = os.getenv("LONGITUDE")
  latitude = os.getenv("LATITUDE")


def time_date():
  day = date.today()
  return day
  