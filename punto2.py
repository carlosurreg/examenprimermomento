LIMITADOR=2
cont=0

#LISTAS
frutas=[]

#DICCIONARIO
fruta={}

while(cont < LIMITADOR):
    fruta["nombre"]=input("Digite nombre: ")
    fruta['precio']=input("Digite su precio: ")
    fruta['color']=input("Digite su color: ")
    cont+= 1
    frutas.append(fruta)

frutas.reverse()
print(F'{frutas}')


    
    
        


