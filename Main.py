import Account
import Reg
import Log
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp

kv = Builder.load_file
kv("Account.kv")
kv("Reg.kv")
kv("Log.kv")
kv("Admin.kv")


class MyApp(MDApp):
    def build(self):

        screen_manager = ScreenManager()
        screen_manager.add_widget(Log.LogPage(name="LogPage"))
        screen_manager.add_widget(Reg.RegPage(name="RegPage"))
        screen_manager.add_widget(Account.Account(name="Account"))
        return screen_manager


if __name__ == '__main__':
    MyApp().run()
