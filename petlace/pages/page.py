import customtkinter as ctk

from petlace.models import Application


class Page(ctk.CTkFrame):
    def __init__(self, app: Application, **kwargs):
        super().__init__(app, fg_color='white', **kwargs)
        self.router = app.router
