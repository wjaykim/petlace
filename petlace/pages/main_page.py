import customtkinter as ctk
import tkintermapview

from petlace.components import PlaceCard
from petlace.data import places
from .page import Page


class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)

        place_list = ctk.CTkScrollableFrame(self, fg_color='#F0F0F3')
        place_list.pack(side=ctk.LEFT, anchor=ctk.W, expand=True, fill=ctk.BOTH)

        map_widget = tkintermapview.TkinterMapView(self, width=960, height=720, corner_radius=0, bg_color='white')
        map_widget.pack(side=ctk.RIGHT, anchor=ctk.E)

        random_places = places.sample(10)
        for place in random_places.itertuples():
            card = PlaceCard(place_list, place)
            card.pack(side=ctk.TOP, anchor=ctk.W, pady=4)

            map_widget.set_marker(place.lat, place.lon, place.name, text_color='gray14', font=('Roboto', 14, 'bold'))

        lon_list = [place.lon for place in random_places.itertuples()]
        lat_list = [place.lat for place in random_places.itertuples()]
        left_top = (max(lat_list), min(lon_list))
        right_bottom = (min(lat_list), max(lon_list))

        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        map_widget.fit_bounding_box(left_top, right_bottom)
