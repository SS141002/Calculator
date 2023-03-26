from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty


# Window.minimum_height = 500
# Window.minimum_width = 300
Window.size = (650, 500)
Window.custom_titlebar = True
Window.borderless = True

'''
class Calc:
    def __init__(self):
        self.text = ""
        self.infix = []
        self.infix_element = 0

    def insert_into_infix(self, index, number, variable, value):
        self.infix[index] = [number, variable, value]

    def text_to_infix(self):
        num = 0
        for i in self.text:
            if i.isdigit():
                num += (num * 10) + int(i)
            else:
                self.insert_into_infix(self.infix_element, num, '#', '#')
                num = 0

'''


class Arithmetic(Screen):
    pass


class Screen_Manager(ScreenManager):
    pass


class Background(FloatLayout):
    pass


file = Builder.load_file("design.kv")


class MyApp(App):
    def build(self):
        # self.title = "Calculator"
        # self.icon = "ss.ico"
        return Background()


if __name__ == "__main__":
    MyApp().run()
