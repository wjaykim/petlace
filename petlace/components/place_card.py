"""ListPage에서 PlacePage로 연결해주는 장소 카드. ListPage 좌측 toolbar에서 정렬됨."""
import customtkinter as ctk

from petlace.models import find_application
from .web_image import WebImage


class PlaceCard(ctk.CTkFrame):
    def __init__(self, master, place):
        super().__init__(master, fg_color='white', cursor='pointinghand')
        self.place=place

        title = ctk.CTkLabel(self, text=place.name, font=('Roboto Bold', 16))
        title.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(8, 0))

        category = ctk.CTkLabel(self, text=f"{place.category3} · {place.addr1} {place.addr2}",
                                font=('Roboto', 14), text_color='gray52')
        category.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(0, 8))

        # image = WebImage(self, place.image_url, 300, 200)
        # image.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(8, 16))

        # 이벤트 전파를 위해 모든 위젯과 프레임에 바인딩
        for widget in (self, title, category):
            widget.bind("<Button-1>", self.__on_click)

    def __on_click(self, event=None):
        app = find_application(self)

        from petlace.pages import PlacePage
        place_page = PlacePage(app, place=self.place)
        app.router.push(place_page)
