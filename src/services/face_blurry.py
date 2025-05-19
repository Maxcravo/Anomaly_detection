import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import cv2
from cv2.typing import MatLike
from PIL import Image
from utils.model_init import face_model

# https://sayantansamanta098.medium.com/real-time-face-detection-and-blurring-using-python-and-opencv-a0ac39efade2
def face__blurry(frame:MatLike) -> MatLike:
  try:
    results = face_model().predict(frame, conf=0.5, show=True)
    for result in results:
      boxes = result.boxes.xyxy # type: ignore
      for box in boxes:
        # para cada coordenada de cada caixa, transformamos os valores para inteiros
        x1, y1, x2, y2 = int(box[0]), int(box[1]), int(box[2]), int(box[3])
        roi = frame[y1:y2, x1:x2] # pegamos a região do rosto, usando a altura e a largura (cortamos a imagem de y1 até y2(altura) e de x1 até x2(largura))
        face_blur = cv2.GaussianBlur(roi,(99, 99), 90) # aplicamos o blur na imagem na região do rosto
        frame[y1:y2, x1:x2] = face_blur  # pegamos essa região que na qual aplicamos o blur e colocamos de volta na imagem original nos mesmo pontos
    #   frame[y:y+h, x:x+w] = blur
  except Exception as e:
    print(f"Error: {e} in face blurry")
  return frame