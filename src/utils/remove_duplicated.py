from cv2.typing import MatLike

def remove_duplicate(img_list:list[MatLike]): # função que verifica se a imagem não é duplicada
  seen = set()
  unique_imgs = []
  for arr in img_list:
    arr_bytes = arr.tobytes()
    if arr_bytes not in seen:
      seen.add(arr_bytes)
      unique_imgs.append(arr)
  return unique_imgs