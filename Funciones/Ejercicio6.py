# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
import statistics as st

def lista(*num):
    media= st.mean(num)
    return media

print(lista(1, 2, 6, 7, 3, 10))



