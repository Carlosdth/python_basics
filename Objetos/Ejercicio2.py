#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. 
# Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class calculadora():
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma (self):
        suma = self.valor1 + self.valor2
        print(suma)


operacion = calculadora(3, 4)

operacion.suma