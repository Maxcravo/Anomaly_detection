from cv2.typing import MatLike
import cv2
def compress_img(img:MatLike) -> MatLike:
  """Compressing the image trying reducing the size for storage"""
  encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
  result, encimg = cv2.imencode('.jpg', img, encode_param)
  if result == False:
    raise Exception("Error in image compression")
  if result == True:
    return encimg