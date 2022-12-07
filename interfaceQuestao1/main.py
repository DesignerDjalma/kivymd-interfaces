from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

from funcoes import tradutorDeMensagem
from funcoes import destradutorDeMensagem
from funcoes import retornaNomeUsuario

fatorEscala = 1.4
Window.size = (350 * fatorEscala, 580 * fatorEscala)


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

class TelaAjuda(Screen):
    pass

class InterfaceApp(MDApp):
    pass



if __name__ == "__main__":
    InterfaceApp().run()

