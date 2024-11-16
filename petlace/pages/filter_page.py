import customtkinter as ctk
import pandas as pd

from petlace.data import places
from petlace.components import MainLogo, BackButton
from .page import Page
from .list_page import ListPage

class FilterPage(Page):
    def __init__(self, master, places: pd.DataFrame, query='목록'):
        super().__init__(master)

        self.places = places
        self.query = query
        self.filter1 = pd.Series([True] * len(self.places), index=self.places.index)
        self.filter2 = pd.Series([True] * len(self.places), index=self.places.index)
        self.filter3 = pd.Series([True] * len(self.places), index=self.places.index)

        self.filter1_active = False
        self.filter2_active = False
        self.filter3_active = False
        self.filter4_active = True  # 기본 설정으로 활성화

        # 뒤로가기 버튼
        back_button = BackButton(self, router=self.router)
        back_button.pack(side=ctk.TOP, anchor=ctk.W, padx=8, pady=8)

        # 메인 로고 추가
        logo = MainLogo(self)
        logo.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=(60, 30))

        # 텍스트 추가
        text = ctk.CTkLabel(self, text='추가 요구사항이 있나요?', font=('Roboto Bold', 16))
        text.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=10)

        # 수평으로 콤보박스를 배치할 프레임 생성
        combo_frame1 = ctk.CTkFrame(self)
        combo_frame1.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=8)
        combo_frame2 = ctk.CTkFrame(self)
        combo_frame2.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=8)

        # 필터 버튼 초기화
        self.filter_button1 = self.__initialize_filter_button(combo_frame1, "주차 가능", lambda: self.__toggle_filter('filter1', self.filter_button1, 'parking', 'Y'))
        self.filter_button2 = self.__initialize_filter_button(combo_frame1, "대형견 가능", lambda: self.__toggle_filter('filter2', self.filter_button2, 'petSize', '모두 가능'))
        self.filter_button3 = self.__initialize_filter_button(combo_frame2, "추가요금 없음", lambda: self.__toggle_filter('filter3', self.filter_button3, 'extraFee', '없음'))
        self.filter_button4 = self.__initialize_filter_button(combo_frame2, "요구사항 없음", self.__reset_filters, active=True)

        # 검색 버튼 생성
        search_button = ctk.CTkButton(self, text='검색', command=self.__on_click_search)
        search_button.pack(side=ctk.TOP, anchor=ctk.CENTER, pady=20)

    def __initialize_filter_button(self, parent, text, command, active=False):
        """필터 버튼을 초기화하고 기본 상태를 설정하는 헬퍼 메서드"""
        button = ctk.CTkButton(parent, text=text, command=command)
        button.pack(side=ctk.LEFT, pady=5)
        button.configure(fg_color="blue" if active else "gray")
        return button

    def __toggle_filter(self, filter_name, button, condition_column, condition_value):
        """공통 필터 토글 메서드로 필터 상태 및 버튼 색상 변경"""
        filter_active_attr = f"{filter_name}_active"
        is_active = getattr(self, filter_active_attr)
        setattr(self, filter_active_attr, not is_active)
        button.configure(fg_color="blue" if not is_active else "gray")
        
        if not is_active:
            setattr(self, filter_name, (self.places[condition_column] == condition_value))
            self.__deactivate_filter4()
        else:
            setattr(self, filter_name, pd.Series([True] * len(self.places), index=self.places.index))
            self.__check_all_filters()

    def __deactivate_filter4(self):
        # 다른 필터가 활성화되면 filter4 비활성화
        self.filter4_active = False
        self.filter_button4.configure(fg_color="gray")

    def __check_all_filters(self):
        # 모든 필터가 비활성화되면 filter4 활성화
        if not self.filter1_active and not self.filter2_active and not self.filter3_active:
            self.filter4_active = True
            self.filter_button4.configure(fg_color="blue")

    def __reset_filters(self):
        # 모든 필터 초기화 및 다른 필터 버튼 비활성화
        self.filter1_active = False
        self.filter2_active = False
        self.filter3_active = False
        self.filter_button1.configure(fg_color="gray")
        self.filter_button2.configure(fg_color="gray")
        self.filter_button3.configure(fg_color="gray")
        self.filter1 = pd.Series([True] * len(self.places), index=self.places.index)
        self.filter2 = pd.Series([True] * len(self.places), index=self.places.index)
        self.filter3 = pd.Series([True] * len(self.places), index=self.places.index)

        # filter_button4 활성화
        self.filter4_active = True
        self.filter_button4.configure(fg_color="blue")

    def __on_click_search(self):
        # 필터링된 장소를 검색
        filtered_places = self.places[self.filter1 & self.filter2 & self.filter3]
        list_page = ListPage(self.master, places=filtered_places, query=self.query)
        self.router.push(list_page)
