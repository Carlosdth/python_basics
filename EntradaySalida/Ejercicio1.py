from math import sqrt


A= int(input("Ingrese un numero A: "))
B= int(input("Ingrese un numero B: "))
C= int(input("Ingrese un numero C: "))

x1= 0
x2= 0

if ((B**2) - (4*A*C)) < 0:
    print("No se puede resolver")

else:
    x1= (-B + sqrt((B**2) - (4*A*C))) / (2*A)
    x2= (-B - sqrt((B**2) - (4*A*C))) / (2*A)

print("La solucion es:", x1)   
print("La solucion es:", x2)
