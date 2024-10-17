import customtkinter as ctk

from petlace.data import places
from .list_page import ListPage
from .page import Page


class MainPage(Page):
    def __init__(self, master):
        super().__init__(master)

        text = ctk.CTkLabel(self, text='Welcome to Petlace!', font=('Roboto Bold', 16))
        text.pack(side=ctk.TOP, anchor=ctk.W)

        addr1_list = sorted(places['addr1'].unique())
        combo_addr1 = ctk.CTkComboBox(self, values=addr1_list, command=self.__on_addr1_selected)
        combo_addr1.pack(side=ctk.TOP, anchor=ctk.W)
        self.combo_addr1 = combo_addr1

        combo_addr2 = ctk.CTkComboBox(self, values=[], command=self.__on_addr2_selected)
        combo_addr2.pack(side=ctk.TOP, anchor=ctk.W)
        self.combo_addr2 = combo_addr2
        self.__on_addr1_selected(combo_addr1.get())

        search_button = ctk.CTkButton(self, text='검색', command=self.__on_click_search)
        search_button.pack(side=ctk.TOP, anchor=ctk.W)

    def __on_click_search(self):
        addr2 = self.combo_addr2.get()
        print(addr2)
        list_page = ListPage(self.master,
                             places=places[places['addr2'] == addr2].head(10),
                             query=f"{addr2} 목록")
        self.router.push(list_page)

    def __on_addr1_selected(self, value):
        filtered_addr2 = sorted(places[places['addr1'] == value]['addr2'].unique())

        self.combo_addr2.configure(values=filtered_addr2)
        self.combo_addr2.set(filtered_addr2[0])

    def __on_addr2_selected(self, value):
        pass