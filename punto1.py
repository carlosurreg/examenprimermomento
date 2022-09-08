numero = int(input("Digita cantidad de números: "))
contador=0
contadorMultiplos2=0
contadorMultiplos3=0
while(contador<numero):
    elemento = int(input("Digita  número: "))
       
    contador=contador+1
       
    if(elemento %3==0 and elemento%2==0):
        contadorMultiplos2+=1
        contadorMultiplos3+=1
        print(f'{elemento} es multiplo 2 y de 3')
    elif(elemento%2==0):
         contadorMultiplos2+=1
         print(f'{elemento} es multiplo 2 ')
    elif(elemento%3==0):
        contadorMultiplos3+=1
        print(f'{elemento} es multiplo 3 ')   
    else:
        print(f'El numero no es multiplo de 2 y de 3')     

print(f'El numero de multiplos 2 ingresados fue de {contadorMultiplos2}')     
print(f'El numero de multiplos 3 ingresados fue de {contadorMultiplos3}')