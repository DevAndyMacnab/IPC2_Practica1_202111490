from mailbox import NoSuchMailboxError


class Pedidos():
    def __init__(self,nombre,cantidad,ingredientes) :
        self.nombre= nombre
        self.cantidad= cantidad
        self.ingredientes= ingredientes
        self.siguiente= None
        self.anterior=None
         
        
        