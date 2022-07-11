palabra1= input("Introduce la palabra 1: ")
palabra2= input("Introduce la palabra2: ")


if palabra1[-3:] == palabra2[-3:]:
    print("Riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("Riman un poco")
else:
    print("NO riman")