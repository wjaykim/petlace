import customtkinter as ctk

from petlace.data import places
from .list_page import ListPage
from .page import Page


class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)

        text = ctk.CTkLabel(self, text='Welcome to Petlace!', font=('Roboto Bold', 16))
        text.pack(side=ctk.TOP, anchor=ctk.W)

        def on_click_button():
            list_page = ListPage(master, places.sample(10))
            self.router.push(list_page)

        button = ctk.CTkButton(self, text='추천 장소', command=on_click_button)
        button.pack(side=ctk.TOP, anchor=ctk.W)
