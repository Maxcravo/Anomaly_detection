from cv2.typing import MatLike
from numpy.typing import NDArray
import numpy as np
import cv2

def compress_img(img:MatLike) -> NDArray[np.uint8] | str:
  """Compressing the image trying reducing the size for storage"""
  encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
  result, encimg = cv2.imencode('.jpg', img, encode_param)
  if result == False:
    raise Exception("Error in image compression")
  if result == True:
    return encimg
  return "Error in image compression"