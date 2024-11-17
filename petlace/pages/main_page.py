"""1번째 페이지. 장소 필터링."""
import customtkinter as ctk

from petlace.data import places
from petlace.components import MainLogo
from .list_page import ListPage
from .page import Page


class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)

        # logo = MainLogo(self)
        # logo.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(80,30))

        text = ctk.CTkLabel(self, text='어느 지역을 여행하시나요?', font=('Roboto Bold', 16))
        text.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(30,20))
        
         # 수평으로 콤보박스를 배치할 프레임 생성
        combo_frame = ctk.CTkFrame(self)
        combo_frame.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=8)  # 프레임 위치 설정
        
        addr1_list = sorted(places['addr1'].unique())
        combo_addr1 = ctk.CTkComboBox(combo_frame, values=addr1_list, command=self.__on_addr1_selected)
        combo_addr1.pack(side=ctk.LEFT, padx=5)
        self.combo_addr1 = combo_addr1

        combo_addr2 = ctk.CTkComboBox(combo_frame, values=[], command=self.__on_addr2_selected)
        combo_addr2.pack(side=ctk.LEFT, padx=5)
        self.combo_addr2 = combo_addr2
        self.__on_addr1_selected(combo_addr1.get())

        search_button = ctk.CTkButton(self, text='검색', command=self.__on_click_search)
        search_button.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=20)

    def __on_click_search(self):
        addr1 = self.combo_addr1.get()
        addr2 = self.combo_addr2.get()

        # 필터링된 장소를 검색
        filtered_places = places[(places['addr1'] == addr1) & (places['addr2'] == addr2)]
        list_page = ListPage(self.master, places=filtered_places, query=f"{addr2} 목록")
        self.router.push(list_page)

    def __on_addr1_selected(self, value):
        filtered_addr2 = sorted(places[places['addr1'] == value]['addr2'].unique())

        self.combo_addr2.configure(values=filtered_addr2)
        self.combo_addr2.set(filtered_addr2[0])

    def __on_addr2_selected(self, value):
        pass