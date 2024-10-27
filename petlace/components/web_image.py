"""places 파일에서 Image_url로 웹에서 이미지 추출"""
import io
from concurrent.futures import ThreadPoolExecutor

import customtkinter as ctk
import requests
from PIL import Image, ImageTk, ImageOps


class WebImage(ctk.CTkCanvas):
    executor = ThreadPoolExecutor(max_workers=5)

    def __init__(self, master, image_url:str, width: int, height: int):
        super().__init__(master=master, width=width, height=height, highlightthickness=0)
        self.image = None

        if image_url == '': return

        WebImage.executor.submit(self.process, image_url=image_url, width=width, height=height)

    def process(self, image_url, width, height):
        raw_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(raw_data))
        image = ImageOps.cover(image, (width, height))
        self.image = ImageTk.PhotoImage(image)
        self.create_image(0, 0, anchor=ctk.NW, image=self.image)
