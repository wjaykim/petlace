import customtkinter as ctk

from .page import Page

class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text='Petlace')
        title.pack(side=ctk.TOP, anchor=ctk.W)