import getpass
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout

fatorEscala = 1.4
Window.size = (350 * fatorEscala, 580 * fatorEscala)

class TelaInicial(Screen):
    pass


class TelaPrincipal(Screen):
    def on_enter(self):
        self.ids.nomeDetetive.text = f"Detetive: {getpass.getuser().upper()}"

class InterfaceApp(MDApp):
    def build(self):
        interface = Builder.load_file("./interface.kv")
        return interface


if __name__ == "__main__":
    InterfaceApp().run()
