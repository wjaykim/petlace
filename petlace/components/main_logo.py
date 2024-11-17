"MainPage 로고"
import customtkinter as ctk
from PIL import Image, ImageTk

from petlace.utils import get_file


class MainLogo(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # 이미지 경로 설정 및 로드
        logo_image = Image.open(get_file("assets/logo.png"))
        self.original_logo_image = logo_image.resize((200, 200), Image.Resampling.LANCZOS)
        self.logo_image = self.original_logo_image.copy()
        self.logo = ImageTk.PhotoImage(self.logo_image)
        
        # 이미지 표시를 위한 라벨 생성
        self.logo_label = ctk.CTkLabel(self, image=self.logo, text="")
        self.logo_label.pack(expand=True)
