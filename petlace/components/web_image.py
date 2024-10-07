import io
import threading

import customtkinter as ctk
import requests
from PIL import Image, ImageTk, ImageOps


class WebImage(ctk.CTkCanvas):
    def __init__(self, master, image_url:str, width: int, height: int):
        super().__init__(master=master, width=width, height=height, highlightthickness=0)
        self.image = None

        if image_url == '': return

        thread = threading.Thread(target = self.process, args = (image_url, width, height))
        thread.start()

    def process(self, image_url, width, height):
        raw_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(raw_data))
        image = ImageOps.cover(image, (width, height))
        self.image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, anchor=ctk.NW, image=self.image)
