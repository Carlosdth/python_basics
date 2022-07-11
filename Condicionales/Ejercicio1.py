letra= input("Introduce una letra: ")

if letra.lower() == "a":
    print("Es una vocal")
elif letra.lower() == "e":
    print("Es una vocal")
elif letra.lower() == "i":
    print("Es una vocal")
elif letra.lower() == "o":
    print("Es una vocal")
elif letra.lower() == "u":
    print("Es una vocal")
else:
    print("NO es una vocal")


# Forma mas facil de hacerlo

if letra.lower() in "aeiou":
    print("Es una Vocal")
else:
    print("NO es una vocal")