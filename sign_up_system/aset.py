from PIL import Image, ImageTk

def load_image(path, size):
   img = Image.open(path)
   img = img.resize(size)
   return ImageTk.PhotoImage(img)

class Aset:
   def __init__(self):
      self.label_img = load_image("sign_up_system/aset/bird.jpg", (400,540))
      self.red_dot = load_image("sign_up_system/aset/reddot.png", (7,7))