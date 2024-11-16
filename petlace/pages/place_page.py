"""3번째 페이지. place card 선택 시 나타남. 장소에 대한 상세정보 제공"""

import customtkinter as ctk
import webbrowser
from petlace.components import WebImage, BackButton
from .page import Page


class PlacePage(Page):
    def __init__(self, master, place):
        super().__init__(master)
        
        # 뒤로가기 버튼
        back_filter_1 = BackButton(self, router=self.router)
        back_filter_1.pack(side=ctk.TOP, anchor=ctk.W, padx=8, pady=8)

        # 이미지
        image = WebImage(self, place.image_url, 300, 200)
        image.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(8, 16))

        # 장소
        title = ctk.CTkLabel(self, text=place.name, font=('Roboto Bold', 16))
        title.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(16, 0))

        address = ctk.CTkLabel(self, text=place.addr, font=('Roboto', 14), text_color='gray52', justify='left', wraplength=350)
        address.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        
        #필터 표시
        filter_frame = ctk.CTkFrame(self)
        filter_frame.pack(side=ctk.TOP, anchor=ctk.W, pady=8)

        filter_1 = ctk.CTkButton(filter_frame, text="주차 가능")
        filter_1.pack(side=ctk.LEFT, pady=5)
        filter_1.configure(fg_color="blue" if place.parking == "Y" else "gray")

        filter_2 = ctk.CTkButton(filter_frame, text="대형견 가능")
        filter_2.pack(side=ctk.LEFT, pady=5)
        filter_2.configure(fg_color="blue" if place.petSize == "모두 가능" else "gray")

        filter_1 = ctk.CTkButton(filter_frame, text="추가요금 없음")
        filter_1.pack(side=ctk.LEFT, pady=5)
        filter_1.configure(fg_color="blue" if place.extraFee == "없음" else "gray")

        # 상세설명
        category = ctk.CTkLabel(self, text=
                                f"전화번호: {place.callNum} \n"
                                f"홈페이지: {place.webSite} \n"
                                f"운영시간: {place.openTime} \n"
                                f"길찾기: {place.nmap_url} \n"
                                f"반려동물 제한사항: {place.petRule} \n",
                                font=('Roboto', 14), text_color='gray52', justify='left', wraplength=350)
        category.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        if place.petSize != "모두 가능":
            petsize = ctk.CTkLabel(self, text=f"입장 가능 동물 크기: {place.petSize}", font=('Roboto', 14), text_color='gray52', justify='left', wraplength=350)
            petsize.pack(side=ctk.TOP, anchor=ctk.W, padx=16)
        if place.extraFee != "없음":
            extrafee = ctk.CTkLabel(self, text=f"애견 동반 추가 요금: {place.extraFee}", font=('Roboto', 14), text_color='gray52', justify='left', wraplength=350)
            extrafee.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        
        # 이미지 클릭 시 네이버지도 웹 연결
        image.bind("<Button-1>", lambda e: webbrowser.open(place.nmap_url))

        
