from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from funcoes import tradutorDeMensagem
from funcoes import destradutorDeMensagem
from funcoes import retornaNomeUsuario

from tkinter.filedialog import asksaveasfile 
from tkinter.messagebox import showinfo

fatorEscala = 1.4
Window.size = (360 * fatorEscala, 640 * fatorEscala)

class TelaInicial(Screen):
    pass
class TelaSalvar(Screen):
    pass

class TelaAjuda(Screen):
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
        tipos = (('texto', '*.txt'),('Todos os arquivos', '*.*'))
        arquivo = asksaveasfile(title="Salvar Codigos Secretos",filetypes=tipos,confirmoverwrite=True)
        if arquivo:
            with open(file=arquivo.name, mode='a') as arq:
                arq.write(f"{self.ids.mensagemFinal.text}\n")
            showinfo(title="Sucesso", message="Seu código foi salvo com Sucesso")

class InterfaceApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"

if __name__ == "__main__":
    InterfaceApp().run()
