class Mensagem:
    def __init__(self, id, mensagem, usuario, usuarioFinal):
        self.id = id
        self.mensagem =  mensagem
        self.usuario = usuario
        self.usuarioFinal = usuarioFinal
    
    def __str__(self):
        return f"id: {self.id}, mensagem: {self.mensagem}, usuário: {self.usuario}, usuarioFinal: {self.usuarioFinal}"
    
def serializar(msg):
    return {"id": str(msg.id), "mensagem": msg.mensagem, "usuario": msg.usuario, "usuarioFinal": msg.usuarioFinal}

    
