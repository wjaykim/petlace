"""3번째 페이지. place card 선택 시 나타남. 장소에 대한 상세정보 제공"""

import customtkinter as ctk
import webbrowser
from petlace.components import WebImage, BackButton
from .page import Page


class PlacePage(Page):
    def __init__(self, master, place):
        super().__init__(master)
        
        # 뒤로가기 버튼
        back_button = BackButton(self, router=self.router)
        back_button.pack(side=ctk.TOP, anchor=ctk.W, padx=8, pady=8)

        # 장소
        title = ctk.CTkLabel(self, text=place.name, font=('Roboto Bold', 16))
        title.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(16, 0))
        
        # 상세설명
        category = ctk.CTkLabel(self, text=f"{place.category3} · {place.addr} \n" 
                                f"전화번호: {place.callNum} \n"
                                f"홈페이지: {place.webSite} \n"
                                f"운영시간: {place.openTime} \n"
                                f"네이버지도: {place.nmap_url} \n"
                                f"입장 가능 동물 크기: {place.petSize} \n"
                                f"반려동물 제한사항: {place.petRule} \n"
                                f"애견 동반 추가 요금: {place.extraFee} \n",
                                font=('Roboto', 14), text_color='gray52', justify='left')
        category.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        # 이미지
        image = WebImage(self, place.image_url, 300, 200)
        image.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(8, 16))
        
        # 이미지 클릭 시 네이버지도 웹 연결
        image.bind("<Button-1>", lambda e: webbrowser.open(place.nmap_url))

        
