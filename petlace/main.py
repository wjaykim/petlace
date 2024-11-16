"""메인 구동 파일. 기본 프레임과 프로그램 실행&종료 관련 설정."""
import os
import sys

# Windows에서만 발생하는 오류 수정
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import customtkinter as ctk
from dotenv import load_dotenv

from petlace.models import Application, Router
from petlace.pages import Page, MainPage

load_dotenv(dotenv_path='../.env')

class MainApplication(Application):
    def __init__(self):
        super().__init__()
        self.__router = Router()
        self.__router.add_page_change_listener(self.__on_page_change)

        self.title('Petlace')
        self.geometry('375x667+0+0')

        self.root_frame = ctk.CTkFrame(self)
        self.root_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        main_page = MainPage(self)
        self.router.push(main_page)

    @property
    def router(self):
        return self.__router

    def __on_page_change(self, page: Page):
        page.place(in_=self.root_frame, x=0, y=0, relwidth=1, relheight=1)
        page.lift()

app = None

def launch():
    global app
    ctk.set_appearance_mode('light')

    theme_path = os.path.join(os.path.dirname(__file__), 'theme.json')
    ctk.set_default_color_theme(theme_path)

    app = MainApplication()
    app.mainloop()

def destroy():
    if isinstance(app, MainApplication):
        app.destroy()

if __name__ == "__main__":
    launch()
