import getpass
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window


fatorEscala = .65
w = 1280 * fatorEscala
h = 720 * fatorEscala
Window.size = (h,w)

class SegundaInterfaceApp(MDApp):
    def build(self):
        interface = Builder.load_file("./segundainterface.kv")
        return interface


if __name__ == "__main__":
    SegundaInterfaceApp().run()
