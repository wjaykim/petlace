from abc import abstractmethod

import customtkinter as ctk
import tkinter as tk

from .router import Router


class Application(ctk.CTk):
    @property
    @abstractmethod
    def router(self) -> Router:
        pass

def findApplication(widget: tk.Misc):
    if isinstance(widget.master, Application):
        return widget.master
    return findApplication(widget.master)
