
from cola import ColaEnlazada

#Archivo principal del programa
salida=False
print("BIENVENIDO A LA TIENDA DE HOCHOS")
print("PARA SALIR DE LA TIENDA ESCRIBA: salir")
print("PARA INGRESAR UN PEDIDO ESCRIBA: pedido")
print("PARA DESPACHAR UN PEDIDO, ESCRIBA: despacho")
print("PARA VER COMO VA LA COLA, ESCRIBA: ver")
print("PARA VER LOS DATOS DEL DESARROLLADOR, ESCRIBA, dev")
ingredientesLista=[]
pedidos=ColaEnlazada()
while salida==False:
    opcion=input("elija una opcion...")
    
    if opcion =='salir':
        salida=True
    
    if opcion=='dev':
        print("-----------------------------")
        print("NOMBRE: Andy Roberto Jimenez Macnab")
        print("CARNET: 202111490")
    
    if opcion =='pedido':
        
        print("-----------------------------")
        name=input("ingrese su nombre...")
        amount=input("ingrese la cantidad...")
        cantidadIngredientes=input("¿Cuantos ingredientes desea ingresar...?")
        ingredientesLista=[]
        for cantidad in range(int(cantidadIngredientes)):
            ingredientes=input("ingrese el ingrediente...")
            ingredientesLista.append(ingredientes)
            print(ingredientesLista)
        #mostrar la cola en pantalla y dar por parametro estos datos
        pedidos.agregarFinal(name,int(amount),ingredientesLista)
        pedidos.recorrerInicioFin()
        
        
    if opcion =='despacho':
        print("-----------------------------")
        pedidos.eliminarFinal()
        pedidos.recorrerInicioFin()
        
    if opcion=='ver':
        pedidos.crearReporte()
        
        
        
        
    