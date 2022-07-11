# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

numero= int(input('Dime un numero: '))
i = 0

while i < 10:
    
    i += 1
    multiplicar= numero * i
    
    print('{} por {} es: {}'.format(i, numero, multiplicar))