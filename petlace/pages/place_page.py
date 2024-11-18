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
        image = WebImage(self, place.image_url, master.winfo_width(), int(master.winfo_width() / 16 * 9))
        image.pack(side=ctk.TOP, anchor=ctk.W, fill=ctk.X)

        image_label = ctk.CTkLabel(self, text='사진을 클릭하면 네이버 지도로 연결됩니다', font=('Roboto Bold', 10))
        image_label.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        # 장소
        title = ctk.CTkLabel(self, text=place.name, font=('Roboto Bold', 16))
        title.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=(16, 0))

        address = ctk.CTkLabel(self, text=f"{place.category3} · {place.addr}", font=('Roboto', 14), text_color='gray52', justify='left', wraplength=350)
        address.pack(side=ctk.TOP, anchor=ctk.W, padx=16)
        
        #필터 표시
        filter_frame = ctk.CTkFrame(self)
        filter_frame.pack(side=ctk.TOP, anchor=ctk.W, padx=16, pady=8)

        filter_1 = AvailabilityLabel(filter_frame, text_yes="주차 가능", text_no="주차 불가능", available=place.parking == "Y")
        filter_1.pack(side=ctk.LEFT, padx=(0, 8))

        filter_2 = AvailabilityLabel(filter_frame, text_yes="대형견 가능", text_no="대형견 불가능", available=place.petSize == "모두 가능")
        filter_2.pack(side=ctk.LEFT, padx=(0, 8))

        filter_3 = AvailabilityLabel(filter_frame, text_yes="추가요금 없음", text_no="추가요금 있음", available=place.extraFee == "없음")
        filter_3.pack(side=ctk.LEFT, padx=(0, 8))

        # 상세설명
        category = ctk.CTkLabel(self, text=
                                f"전화번호: {place.callNum} \n"
                                f"운영시간: {place.openTime} \n"
                                f"반려동물 제한사항: {place.petRule} \n",
                                font=('Roboto', 14), text_color='gray52', justify='left')
        category.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        homepage = ctk.CTkLabel(self, text=f"홈페이지: {place.webSite}", font=('Roboto', 14), text_color='blue', justify='left')
        homepage.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        if place.petSize != "모두 가능":
            petsize = ctk.CTkLabel(self, text=f"입장 가능 동물 크기: {place.petSize}", font=('Roboto', 14), text_color='gray52', justify='left')
            petsize.pack(side=ctk.TOP, anchor=ctk.W, padx=16)
        if place.extraFee != "없음":
            extrafee = ctk.CTkLabel(self, text=f"애견 동반 추가 요금: {place.extraFee}", font=('Roboto', 14), text_color='gray52', justify='left')
            extrafee.pack(side=ctk.TOP, anchor=ctk.W, padx=16)

        
        # 이미지 클릭 시 네이버지도 웹 연결
        image.bind("<Button-1>", lambda e: webbrowser.open(place.nmap_url))
        homepage.bind("<Button-1>", lambda e: webbrowser.open(place.webSite))

class AvailabilityLabel(ctk.CTkFrame):
    def __init__(self, parent, text_yes, text_no, available):
        super().__init__(parent, width=100, border_width=2, border_color="#26C6DA" if available else "#BDBDBD", corner_radius=6)
        label = ctk.CTkLabel(self, text=text_yes if available else text_no)
        label.pack(side=ctk.TOP, padx=8, pady=4)
