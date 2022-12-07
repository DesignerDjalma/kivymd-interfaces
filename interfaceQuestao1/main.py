from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from funcoes import tradutorDeMensagem
from funcoes import destradutorDeMensagem
from funcoes import retornaNomeUsuario

fatorEscala = 1.4
Window.size = (350 * fatorEscala, 580 * fatorEscala)

class TelaSalvar(Screen):
    pass

class TelaInicial(Screen):
    pass

class TelaPrincipal(Screen):
    def on_enter(self, *args) -> None:
        self.ids.nomeDetetive.text = f"Detetive: {retornaNomeUsuario()}"
        pass

    def traduzir(self) -> None:
        self.ids.mensagemFinal.text = tradutorDeMensagem(
            self.ids.mensagemInicial.text)

    def codificar(self) -> None:
        self.ids.mensagemFinal.text = destradutorDeMensagem(
            self.ids.mensagemInicial.text)

    def salvar(self) -> None:
        from kivy.uix.popup import Popup
        self.janela = Popup(title="Hello")


class TelaAjuda(Screen):
    pass

class InterfaceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "Red"  # "Purple", "Red"


if __name__ == "__main__":
    InterfaceApp().run()

