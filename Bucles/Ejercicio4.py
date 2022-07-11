# Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares

num1= int(input('Ingresa un numero: '))
num2= int(input('Ingresa otro numero: '))

for i in range(num1, num2):
    if i % 2 == 0:
        continue
    print(i)