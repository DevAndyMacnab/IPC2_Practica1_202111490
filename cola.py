import os
from subprocess import TimeoutExpired
from pedidos import Pedidos

class ColaEnlazada():
    def __init__(self):
        self. primero=None
        self.ultimo=None
        self.tiempo=0
        self.despacho=0
        
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
            
            
        tiempo=0
        despacho=0
        for ingrediente in ingredientes:
            if ingrediente == 'salchicha':
                tiempo=tiempo + 2
            elif ingrediente=='chorizo':
                tiempo=tiempo +3
                
            elif ingrediente=='salami':
                tiempo=tiempo + 1.5
            elif ingrediente=='longaniza':
                tiempo=tiempo + 4
            elif ingrediente=='costilla':
                tiempo=tiempo + 6
            
        tiempo=tiempo * cantidad
        self.ultimo.tiempo=tiempo
        
        while
        
        
        
        self.unirNodos()
        
    def recorrerInicioFin(self):
        tmp=self.primero
        while tmp:
            print(tmp.nombre,tmp.cantidad, "shucos de:",tmp.ingredientes,"demorará",tmp.tiempo,"minutos...", tmp.despacho)
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
            print("no se pudo")
            self.primero=self.ultimo=None
                
        else:
            self.primero=self.primero.siguiente
        self.unirNodos()
        
    def eliminarFinal(self):
        if self.estaVacia():
            print("LA COLA YA SE ENCUENTRA VACIA")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
                
        else:
            self.primero=self.primero.siguiente
        self.unirNodos()
        
    def reporte(self):
        aux=self.primero
        text=''
        text+='rankdir=LR; \n'
        text+="node[shape=egg, style=filled, color=khaki, fontname=\"Century Gothic\"];  graph [fontname = \"Century Gothic\"];"
        text+="labelloc=\"t; \"label = \"SHUCOS\";\n"
        
        while aux:
            text+="x"+str(aux.nombre)+"[dir=both label=\"Nombre ="+str(aux.nombre)+"\\nCantidad = "+str(aux.cantidad)+" \\nIngredientes = "+str(aux.ingredientes)+ "\"]"
            text+="x"+str(aux.nombre)+"-> x"+str(aux.siguiente.nombre) +"\n"
            text+="x"+str(aux.nombre)+"-> x"+str(aux.anterior.nombre) +"\n"
            aux=aux.siguiente
            if aux!=self.primero:
                text+="x"+str(aux.nombre)+"[dir=both label=\"Cantidad ="+(str(aux.cantidad))+"\\nCantidad = "+str(aux.cantidad)+" \\nIngredientes = "+str(aux.ingredientes)+ "\"]"
                
            if aux==self.ultimo:
                text+="x"+str(aux.nombre)+ "-> x"+str(aux.siguiente.nombre)+"\n"
                text+="x"+str(aux.nombre)+ "-> x"+str(aux.anterior.nombre)+"\n"
                break
        return text
    
    def crearReporte(self):
        contenido="digraph G{\n\n"
        r=open("reporte.txt","w")
        contenido+=str(self.reporte())
        contenido+="\n}"
        r.write(contenido)
        r.close()
        print("done")
        os.system("dot -Tpng reporte.txt -o reporte.png")
        os.system("dot -Tpdf reporte.txt -o reporte.pdf")
        
    
            
        
        
        