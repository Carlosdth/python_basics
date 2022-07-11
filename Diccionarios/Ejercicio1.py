dic= {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

pais= str(input('Dime un pais: '))


if pais.title() in dic:
    print(dic[pais.title()])

else:
    print('Este pais no se encuentra en la lista')

