"""2번째 페이지. 카테고리 분류 및 지도 표시."""
import os

import customtkinter as ctk
import pandas as pd
import tkintermapview

from petlace.components import PlaceCard, BackButton
from .page import Page


class ListPage(Page):
    def __init__(self, master, places: pd.DataFrame, query = '목록'):
        super().__init__(master)

        self.places = places  # 전체 장소 데이터를 저장
        self.filtered_places = places  # 필터된 장소 데이터를 따로 저장

        toolbar = ctk.CTkFrame(self)
        toolbar.pack(side=ctk.TOP, fill=ctk.X)

        back_button = BackButton(toolbar, router=self.router)
        back_button.pack(side=ctk.LEFT, anchor=ctk.W, padx=8, pady=8)

        #제목 생성('~ 목록')
        title = ctk.CTkLabel(toolbar, text=query, font=('Roboto Bold', 16), justify=ctk.CENTER)
        title.pack(side=ctk.LEFT, anchor=ctk.W, expand=True, fill=ctk.X)

        dummy_label = ctk.CTkLabel(toolbar, width=28, height=28, text='')
        dummy_label.pack(side=ctk.LEFT, anchor=ctk.W, padx=8, pady=8)

        self.map_widget = tkintermapview.TkinterMapView(self)
        self.map_widget.pack(fill=ctk.BOTH, expand=True)

        filter_frame = ctk.CTkScrollableFrame(self, orientation='horizontal', height=40)
        filter_frame.pack(side=ctk.TOP, fill=ctk.X, expand=False)

        #카테고리 선택 콤보박스 생성
        category3_list = ['전체'] + sorted(places['category3'].unique())
        combo_category3 = ctk.CTkComboBox(filter_frame, values=category3_list, command=lambda _ : self.__update_filter(), width=120)
        combo_category3.pack(side=ctk.LEFT, anchor=ctk.W, padx=(16, 8), pady=8)
        combo_category3.set("전체")
        self.combo_category3 = combo_category3

        self.filter_parking = FilterButton(filter_frame, "주차 가능", 'parking', 'Y', on_change=self.__update_filter)
        self.filter_parking.pack(side=ctk.LEFT, anchor=ctk.W, padx=(0, 8))
        self.filter_large = FilterButton(filter_frame, "대형견 가능", 'petSize', '모두 가능', on_change=self.__update_filter)
        self.filter_large.pack(side=ctk.LEFT, anchor=ctk.W, padx=(0, 8))
        self.filter_extra = FilterButton(filter_frame, "추가요금 없음", 'extraFee', '없음', on_change=self.__update_filter)
        self.filter_extra.pack(side=ctk.LEFT, anchor=ctk.W, padx=(0, 16))

        self.place_list_frame = ctk.CTkScrollableFrame(self, width=320, fg_color='#F0F0F3')
        self.place_list_frame.pack(side=ctk.TOP, expand=True, fill=ctk.BOTH)

        # 처음에 장소 목록을 표시
        self.display_places()

        #타일 서버 설정(환경변수 활용)
        tile_server_url = os.getenv('TILE_SERVER_URL')
        tile_size = os.getenv('TILE_SIZE')
        if tile_server_url is not None and tile_size is not None:
            self.map_widget.set_tile_server(tile_server_url, tile_size=int(tile_size))
    
    def __update_filter(self):
        category3 = self.combo_category3.get()
        # 선택된 카테고리가 "전체"인 경우 모든 장소를 표시, 아니면 해당 카테고리만 필터링
        condition = pd.Series([True] * len(self.places), index=self.places.index) if category3 == "전체" else self.places['category3'] == category3

        if self.filter_parking.active:
            condition &= (self.places[self.filter_parking.condition_column] == self.filter_parking.condition_value)
        if self.filter_large.active:
            condition &= (self.places[self.filter_large.condition_column] == self.filter_large.condition_value)
        if self.filter_extra.active:
            condition &= (self.places[self.filter_extra.condition_column] == self.filter_extra.condition_value)

        self.filtered_places = self.places[condition]

        self.display_places()


    def display_places(self):
        # 이전에 표시된 모든 장소를 제거
        for widget in self.place_list_frame.winfo_children():
            widget.destroy()
        
        # 지도에서 이전에 표시된 마커 제거
        self.map_widget.delete_all_marker()

        lon_list = []
        lat_list = []

        # 새로운 장소 목록을 표시
        for place in self.filtered_places.itertuples():
            card = PlaceCard(self.place_list_frame, place)
            card.pack(side=ctk.TOP, anchor=ctk.W, pady=4, fill=ctk.X)

            lon_list.append(place.lon)
            lat_list.append(place.lat)
            self.map_widget.set_marker(place.lat, place.lon, place.name, text_color='gray14', font=('Roboto', 14, 'bold'))

        # 마커에 맞게 지도를 조정
        if len(lon_list) == 1 and len(lat_list) == 1:
            self.map_widget.set_position(lat_list[0], lon_list[0])
            self.map_widget.set_zoom(15)  # 적절한 줌 레벨로 설정
        elif lon_list and lat_list:
            left_top = (max(lat_list), min(lon_list))
            right_bottom = (min(lat_list), max(lon_list))
            self.map_widget.fit_bounding_box(left_top, right_bottom)


class FilterButton(ctk.CTkButton):
    active = False

    def __init__(self, parent, text, condition_column=None, condition_value=None, active=False, on_change=None):
        super().__init__(parent, text=text, command=self.__toggle, fg_color='white', text_color='black', hover_color='#EEEEEE', border_width=2, width=80)
        self.condition_column = condition_column
        self.condition_value = condition_value
        self.on_change = on_change
        self.set_active(active)

    def set_active(self, active):
        self.active = active
        self.configure(border_color="#26C6DA" if active else "#BDBDBD")

    def __toggle(self):
        active = not self.active
        self.set_active(active)
        if self.on_change is not None:
            self.on_change()