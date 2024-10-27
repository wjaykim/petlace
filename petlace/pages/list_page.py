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

        left_panel = ctk.CTkFrame(self)
        left_panel.pack(side=ctk.LEFT, anchor=ctk.W, fill=ctk.Y)

        toolbar = ctk.CTkFrame(left_panel)
        toolbar.pack(side=ctk.TOP, fill=ctk.X)

        back_button = BackButton(toolbar, router=self.router)
        back_button.pack(side=ctk.LEFT, anchor=ctk.W, padx=8, pady=8)

        #제목 생성('~ 목록')
        title = ctk.CTkLabel(toolbar, text=query, font=('Roboto Bold', 16), justify=ctk.CENTER)
        title.pack(side=ctk.LEFT, anchor=ctk.W, expand=True, fill=ctk.X)

        #카테고리 선택 콤보박스 생성
        category3_list = ['전체 선택'] + sorted(places['category3'].unique())
        combo_category3 = ctk.CTkComboBox(toolbar, values=category3_list, command=self.__on_category3_selected)
        combo_category3.pack(side=ctk.LEFT, anchor=ctk.W, padx=8)
        combo_category3.set("Select a category")
        self.combo_category3 = combo_category3

        dummy_label = ctk.CTkLabel(toolbar, width=28, height=28, text='')
        dummy_label.pack(side=ctk.LEFT, anchor=ctk.W, padx=8, pady=8)

        self.place_list_frame = ctk.CTkScrollableFrame(left_panel, width=320, fg_color='#F0F0F3')
        self.place_list_frame.pack(side=ctk.TOP, expand=True, fill=ctk.BOTH)

        self.map_widget = tkintermapview.TkinterMapView(self)
        self.map_widget.pack(fill=ctk.BOTH, expand=True)

        # 처음에 장소 목록을 표시
        self.display_places()

        #타일 서버 설정(환경변수 활용)
        tile_server_url = os.getenv('TILE_SERVER_URL')
        tile_size = os.getenv('TILE_SIZE')
        if tile_server_url is not None and tile_size is not None:
            self.map_widget.set_tile_server(tile_server_url, tile_size=int(tile_size))
    
    def __on_category3_selected(self, event):
        category3 = self.combo_category3.get()
        # 선택된 카테고리가 "전체 선택"인 경우 모든 장소를 표시, 아니면 해당 카테고리만 필터링
        if category3 == "전체 선택":
            self.filtered_places = self.places
        else:
            self.filtered_places = self.places[self.places['category3'] == category3]
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
            card.pack(side=ctk.TOP, anchor=ctk.W, pady=4)

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