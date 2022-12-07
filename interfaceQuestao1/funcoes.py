import string
import getpass

def retornaNomeUsuario() -> str:
    """Retorna o nome do usuário."""
    return getpass.getuser()

def descriptografarMensagem(mensagem: str) -> str:
    mensagem = mensagem.replace("[","").replace("]","").replace(" ","").split(",")
    chave = { str(i):v for i,v in enumerate(f" {string.printable}") }
    return ''.join([chave[i] for i in mensagem if i in chave.keys()])

def criptografarMensagem(mensagem: str) -> str:
    chave = {v:i for i, v in enumerate(f" {string.printable}")}
    return ', '.join([str(chave[i]) for i in [i for i in mensagem] if i])

def tradutorDeMensagem(msgSecreta: str) -> str:
    """Traduz uma mensagem secreta em normal."""
    traduzido = descriptografarMensagem(msgSecreta)
    print(f"\nMensagem traduzida: {traduzido}")
    return traduzido

def destradutorDeMensagem(msgNormal: str) -> str:
    """Traduz uma mensagem normal em secreta."""
    destraduzido = criptografarMensagem(msgNormal)
    print(f"\nMensagem secreta: {destraduzido}")
    return destraduzido