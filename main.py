from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


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
