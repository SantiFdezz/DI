from PIL import Image, ImageTk
from io import BytesIO
import requests

class Cell:
    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        response = requests.get(self.url) 
        img_data = Image.open(BytesIO(response.content))
        self.image_tk = ImageTk.PhotoImage(img_data)
        self.description = description
        ##self.image_tk = (Image.open(img)).resize((100, 100), Image.Resampling.LANCZOS) ## Redimensionar imagen de la celda


