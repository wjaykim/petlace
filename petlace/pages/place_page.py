import customtkinter as ctk

from petlace.components import WebImage
from .page import Page


class PlacePage(Page):
    def __init__(self, master, place):
        super().__init__(master)

        title = ctk.CTkLabel(self, text=place.name, font=('Roboto Bold', 16))
        title.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(16, 0))

        category = ctk.CTkLabel(self, text=f"{place.category3} · {place.addr1} {place.addr2}",
                                font=('Roboto', 14), text_color='gray52')
        category.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        image = WebImage(self, place.image_url, 300, 200)
        image.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(8, 16))
