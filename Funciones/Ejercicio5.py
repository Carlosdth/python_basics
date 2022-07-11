# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura;
# y la otra el area de un circulo con argumento de radio

def cuadrado(base, altura):
    area= base * altura
    return area

def circulo (radio):
    pi= 3.14
    area= pi * radio**2
    return area

print(cuadrado(2, 4))
print(circulo(4))