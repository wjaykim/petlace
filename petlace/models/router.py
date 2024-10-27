"""페이지 전환을 stack type으로 관리함."""
class Router:
    def __init__(self):
        self.pages = []
        self.current_page = None
        self.__listeners = []

    def push(self, page):
        self.pages.append(page)
        self.current_page = page
        self.__notify()

    def back(self):
        if len(self.pages) <= 1: return

        page = self.pages.pop()
        page.destroy()
        self.current_page = self.pages[len(self.pages) - 1]
        self.__notify()

    def add_page_change_listener(self, func):
        self.__listeners.append(func)

    def __notify(self):
        for func in self.__listeners:
            func(self.current_page)