from pywinauto.application import Application as WinApplication #запуск приложения
from fixture.group import GroupHelper

class Application:

    def __init__(self, target):
        self.application = WinApplication(backend="win32").start(target) # win32 - это какая технология используется
        self.main_window = self.application.window(title="Free Address Book") # открытие окна
        self.main_window.wait("visible") # дождаться появления окна
        self.groups = GroupHelper(self)

    def destroy(self):
        self.main_window.close() # закрытие приложения

