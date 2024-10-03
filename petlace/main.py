import customtkinter as ctk
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')

from petlace.pages import MainPage

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1280x720+1920+0')

        MainPage(self).pack(side="top", fill="both", expand=True)

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
