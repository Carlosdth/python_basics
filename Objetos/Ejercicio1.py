# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. 
# Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


class estudiante():
    def __init__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota

    def nombre(self):
        print(self.nombre)
    
    def nota(self):
        if self.nota > 4:
            print('Aprobado')
        else:
            print('Suspenso')

estudiante1= estudiante('Carlos', 4)

estudiante1.nombre
estudiante1.nota
