from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

Window.minimum_height = 500
Window.minimum_width = 300
Window.custom_titlebar = True
# Window.borderless = True


class Arithmetic(Screen):
    pass


file = Builder.load_file("design.kv")

scrmgr = ScreenManager()
scrmgr.add_widget(Arithmetic(name="scr_ari"))


class MyApp(App):
    def build(self):
        self.title = "Calculator"
        # self.icon = "ss.ico"
        return scrmgr


if __name__ == "__main__":
    MyApp().run()
