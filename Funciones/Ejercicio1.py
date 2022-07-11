# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. 
# Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

lista= []

def numeros():
    i= 0
    while i <= 5:
        num= int(input('Dime un numero para agregar a la lista: '))
        i += 1
        lista.append(num)
    

def orden():

    lista.sort()
    lista_par= []
    lista_impar= []
    
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)
    
    print(lista_par)
    print(lista_impar)

numeros()
orden()
