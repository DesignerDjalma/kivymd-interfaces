import getpass
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

fatorEscala = 1.4
Window.size = (350 * fatorEscala, 580 * fatorEscala)

class TelaInicial(Screen):
    pass

class TelaPrincipal(Screen):
    def on_enter(self, *args):
        self.ids.nomeDetetive.text = f"Detetive: {getpass.getuser()}"

class InterfaceApp(MDApp):
    def build(self):
        interface = Builder.load_file("./interface3.kv")
        return interface


if __name__ == "__main__":
    InterfaceApp().run()
