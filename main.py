from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen

from kivy.core.window import Window
from kivy.properties import ObjectProperty

from math import *

Window.minimum_width = 550
Window.minimum_height = 500
Window.size = (550, 500)
# Window.custom_titlebar = True
# Window.borderless = True


class Standard(MDScreen):
    std_text = ObjectProperty(None)
    std_ans = ObjectProperty(None)

    negate = False
    percent = False

    def fast_ans(self):
        string = self.std_text.text

        try:
            ans = eval(string)

            if fabs(ans - floor(ans)) < 0.00000000000001:
                ans = int(ans)

            if self.negate:
                ans *= -1

            if self.percent:
                ans /= 100

        except:
            pass
        else:
            self.std_ans.text = str(ans)

    def text_correct(self):
        string = self.std_text.text

        operators = ["+", "-", "/", "*"]

        try:
            if string[0] in operators and string[0] != "-":
                self.std_text.text = ""
            elif string[-1] in operators and string[-2] in operators:
                self.std_text.text = string[:-1]
            elif string[-1] == "." and string[-2] == ".":
                self.std_text.text = string[:-1]
            elif string[-1] == "." and string[-2] in operators:
                self.fast_ans()    
            else:
                self.fast_ans()
        except:
            pass

    def negation(self):
        self.negate = True
        self.fast_ans()
        self.negate = False

    def percentage(self):
        self.percent = True
        self.fast_ans()
        self.percent = False


class Scientific(MDScreen):
    pass


class Unit_Converter(MDScreen):
    unit_main = ObjectProperty(None)
    unit_primary = ObjectProperty(None)
    unit_secondary = ObjectProperty(None)


class Screen_Manager(MDScreenManager):
    pass


class Background(MDScreen):
    pass


class MyApp(MDApp):
    def build(self):
        self.load_kv("design.kv")
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.material_style = "M3"
        self.title = "Calculator"
        self.icon = "Icons\calculator.png"
        return Background()


if __name__ == "__main__":
    MyApp().run()
