"""메인 구동 파일. 기본 프레임과 프로그램 실행&종료 관련 설정."""
import os
import sys
from threading import Timer

import customtkinter as ctk
from dotenv import load_dotenv

# Windows에서만 발생하는 오류 수정
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from petlace.components import MainLogo
from petlace.models import Application, Router
from petlace.pages import Page, MainPage
from petlace.utils import get_file

load_dotenv(dotenv_path='../.env')

class MainApplication(Application):
    def __init__(self):
        super().__init__()
        self.__router = Router()
        self.__router.add_page_change_listener(self.__on_page_change)

        self.title('Petlace')
        self.geometry('375x667+0+0')
        self.resizable(False, False)

        self.root_frame = ctk.CTkFrame(self)
        self.root_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)

        self.splash = ctk.CTkFrame(self, fg_color='white')
        self.splash.place(in_=self.root_frame, x=0, y=0, relwidth=1, relheight=1)
        logo = MainLogo(self.splash)
        logo.place(relx=0.5, rely=0.5, anchor="center")

        t = Timer(2, self.__finish_splash)
        t.start()

    def __finish_splash(self):
        self.splash.destroy()
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

    theme_path = get_file('theme.json')
    ctk.set_default_color_theme(theme_path)

    app = MainApplication()
    app.mainloop()

def destroy():
    if isinstance(app, MainApplication):
        app.destroy()

if __name__ == "__main__":
    launch()
