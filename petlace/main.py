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
        self.geometry('1280x720+0+0')

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
    ctk.set_default_color_theme("./theme.json")
    app = MainApplication()
    app.mainloop()

def destroy():
    if isinstance(app, MainApplication):
        app.destroy()

if __name__ == "__main__":
    launch()
