from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import getpass

fatorEscala = 1.4
Window.size = (350 * fatorEscala, 580 * fatorEscala)

class TelaInicial(Screen):
    pass

class TelaPrincipal(Screen):
    def on_enter(self, *args):
        self.ids.nomeDetetive.text = f"Detetive: {getpass.getuser()}"
        pass

class TelaAjuda(Screen):
    pass

class InterfaceApp(MDApp):
    pass

if __name__ == "__main__":
    InterfaceApp().run()
