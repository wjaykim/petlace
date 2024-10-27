"""MainApplication의 부모클래스"""
from abc import abstractmethod #추상 메소드(자식 클래스에서 반드시 구현해야하는 메소드) 정의할 때 필요함.

import customtkinter as ctk
import tkinter as tk

from .router import Router


class Application(ctk.CTk):
    @property #==router, 객체의 속성을 읽기 전용으로 사용할 수 있게 함
    @abstractmethod #추상 메소드 정의
    def router(self) -> Router:
        pass

def find_application(widget: tk.Misc): #최상위 애플리케이션 객체 반환 함수
    if isinstance(widget.master, Application):
        return widget.master #애플리케이션 객체 반환
    return find_application(widget.master)
