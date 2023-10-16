class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

    def __str__(self):
        return f"id: {str(self.id)}, nome: {self.nome}"
    
def serializarUsuario(usuario):
    return{"id": str(usuario.id), "nome": usuario.nome}
