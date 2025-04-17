import pandas as pd
import base64
import numpy as np
import cv2
from PIL import Image 

# Read the CSV
df = pd.read_csv("./src/data/csv/test.csv")

# Get the base64 string of the image (assuming column name is 'image')
for index, row in df.iterrows():
  # base64 to bytes
  img_bytes = base64.b64decode(row["image"])
  # Bytes to np.unit8 array using numpy
  img_array = np.frombuffer(img_bytes, dtype=np.uint8)
  # use opencv to decode numpy array to matlike image
  img = cv2.imdecode(img_array, cv2.IMREAD_COLOR_BGR)
  #Use PIL to read the image
  img = Image.fromarray(img)
  img.show()
