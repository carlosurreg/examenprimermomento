opcion=100

print("*****supermercado****")
print("1. Agregar codigo,nombre,precio")
print("2. Mostrar productos seleccionados")
print("3. Buscar codigo y editar precio")
print("4. Buscar por codigo y eliminarlo")
print("0. Salir")

producto={}

productos=[]

while(opcion !=0):

    opcion=int(input("Digite su opcion: "))

    if(opcion==1):

        producto['codigo']=input("Digite el codigo del producto: ")
        producto['nombre']=input("Digite el nombre del producto: ")
        producto['precio']=int(input("Digite el precio del producto: "))
        productos.append(producto)

    elif(opcion==0):
        break
    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        buscar=int(input("Digite el codigo: "))
        for producto in productos:
            if(producto["codigo"]==buscar):
                modificar=int(input("Digitar un nuevo precio: "))
                producto["precio"]=modificar

        
    elif(opcion==4):
        buscar=int(input("Digite el codigo del producto: "))
        for producto in productos:
            if(producto["codigo"]==buscar):
                lista.remove(producto)    
                print ("producto eliminado")
            

            
        
        

