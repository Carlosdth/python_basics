# Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial():
    num= int(input('Dime un numero: '))
    
    for i in range(1, num):
        num *= i
    print(num)
        

factorial()

