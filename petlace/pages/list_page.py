import os

import customtkinter as ctk
import pandas as pd
import tkintermapview

from petlace.components import PlaceCard, BackButton
from .page import Page


class ListPage(Page):
    def __init__(self, master, places: pd.DataFrame):
        super().__init__(master)

        left_panel = ctk.CTkFrame(self)
        left_panel.pack(side=ctk.LEFT, anchor=ctk.W, fill=ctk.Y)

        toolbar = ctk.CTkFrame(left_panel)
        toolbar.pack(side=ctk.TOP, fill=ctk.X)

        back_button = BackButton(toolbar, router=self.router)
        back_button.pack(side=ctk.LEFT, anchor=ctk.W, padx=8, pady=8)

        title = ctk.CTkLabel(toolbar, text="목록", font=('Roboto Bold', 16), justify=ctk.CENTER)
        title.pack(side=ctk.LEFT, anchor=ctk.W, expand=True, fill=ctk.X)

        dummy_label = ctk.CTkLabel(toolbar, width=28, height=28, text='')
        dummy_label.pack(side=ctk.LEFT, anchor=ctk.W, padx=8, pady=8)

        place_list = ctk.CTkScrollableFrame(left_panel, width=320, fg_color='#F0F0F3')
        place_list.pack(side=ctk.TOP, expand=True, fill=ctk.BOTH)

        map_widget = tkintermapview.TkinterMapView(self)
        map_widget.pack(fill=ctk.BOTH, expand=True)

        lon_list = []
        lat_list = []

        for place in places.itertuples():
            card = PlaceCard(place_list, place)
            card.pack(side=ctk.TOP, anchor=ctk.W, pady=4)

            lon_list.append(place.lon)
            lat_list.append(place.lat)
            map_widget.set_marker(place.lat, place.lon, place.name, text_color='gray14', font=('Roboto', 14, 'bold'))

        left_top = (max(lat_list), min(lon_list))
        right_bottom = (min(lat_list), max(lon_list))
        map_widget.fit_bounding_box(left_top, right_bottom)

        tile_server_url = os.getenv('TILE_SERVER_URL')
        tile_size = os.getenv('TILE_SIZE')
        if tile_server_url is not None and tile_size is not None:
            map_widget.set_tile_server(tile_server_url, tile_size=int(tile_size))
