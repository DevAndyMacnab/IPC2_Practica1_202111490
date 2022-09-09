from pickletools import read_unicodestring1
from pedidos import Pedidos

class ColaEnlazada():
    def __init__(self):
        self. primero=None
        self.ultimo=None
        
    def unirNodos(self):
        if self.primero!=None:
            self.primero.anterior=self.ultimo
            self.ultimo.siguiente=self.primero
    
    def estaVacia(self):
        if self.primero==None:
            return True
        else:
            return False
    
    def agregarFinal(self,nombre,cantidad,ingredientes):
        nuevoShuco=Pedidos(nombre,cantidad,ingredientes)
        if self.estaVacia():
            self.primero=self.ultimo=nuevoShuco
        else:
            tmp=self.ultimo
            self.ultimo=tmp.siguiente=nuevoShuco
            self.ultimo.anterior=tmp
        self.unirNodos()
        
    def recorrerInicioFin(self):
        tmp=self.primero
        while tmp:
            print(tmp.nombre,tmp.cantidad, "shucos de:",tmp.ingredientes)
            tmp=tmp.siguiente
            if tmp==self.primero:
                break
            
    def recorrerFinInicio(self):
        tmp=self.ultimo
        while tmp:
            print(tmp.nombre,tmp.cantidad,tmp.ingredientes)
            tmp=tmp.anterior
            if tmp==self.ultimo:
                break
            
    def eliminarInicio(self):
        if self.estaVacia():
            print("LA COLA YA SE ENCUENTRA VACIA")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
                
        else:
            self.primero=self.primero.siguiente
        self.unirNodos()
        
        
        