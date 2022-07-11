A= "rojo"
B="verde"
C="azul"
voto= input("Vota al partido A, B o C: ")

if voto.upper() == "A":
    print("Has votado al partido {}".format(A))
elif voto.upper() == "B":
    print("Has votado al partido {}".format(B))
elif voto.upper() == "C":
    print("Has botado al partido {}".format(C))
else:
    print("Opción erronea")


