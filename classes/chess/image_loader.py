import os
from PIL import Image

class ImageLoader:
  
  @staticmethod
  def load_boards() -> dict:
    images = {}
    
    path = './assets/chess/boards/'
    
    for file in os.listdir(path):
      #print(file[:-4])
      image = Image.open(os.path.join(path, file))
      image = image.convert('RGBA')
      images[file[:-4]] = image
    return images
  
  @staticmethod
  def load_pieces() -> dict:
    images = {}
    
    path = './assets/chess/pieces/'
    
    for file in os.listdir(path):
      image = Image.open(os.path.join(path, file))
      image = image.convert('RGBA').resize((image.width//2, image.height//2))
      images[file[:-4]] = image
    return images
  