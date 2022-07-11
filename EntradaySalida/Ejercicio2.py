p1= float(input("Nota primera prueba: "))
p2= float(input("Nota segunda prueba: "))
p3= float(input("Nota tercera prueba: "))

promedioPractica= (p1+p2+p3)/3
print("El promedio de las practicas es: ", promedioPractica)

examenParcial= float(input("Nota Examen Parcial: "))
examenFinal= float(input("Nota Examen Final: "))

promedio= (promedioPractica + 2*examenParcial + 3*examenFinal) / 6
print("El promedio es: ", promedio)