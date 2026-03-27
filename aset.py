from PIL import Image, ImageTk

def load_image(path, size):
   img = Image.open(path)
   img = img.resize(size)
   return ImageTk.PhotoImage(img)

class Aset:
   def __init__(self):
      self.label_img = load_image("bird.jpg", (370, 480))