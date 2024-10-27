"""뒤로가기 버튼"""
from pathlib import Path

import customtkinter as ctk
from PIL import Image, ImageTk


class BackButton(ctk.CTkButton):
    def __init__(self, master, router, size=22):
        chevron_image = Image.open(str(Path(__file__).resolve().parent.parent) + '/assets/chevron-left.png')
        chevron_image = chevron_image.resize((round(size / 1.6), size), Image.Resampling.LANCZOS)
        back_icon = ImageTk.PhotoImage(chevron_image)
        super().__init__(master,
                         width=size,
                         height=size,
                         text='',
                         image=back_icon,
                         text_color='gray14',
                         fg_color='transparent',
                         hover_color='gray90',
                         command=router.back)
