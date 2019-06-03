## Imprima la suma de la segunda columna.
#leer archivo
file = open('data.csv', 'r').readlines()

#Eliminar \n al final
file = [row[0:-1] for row in file]

#Separar por tab
file = [row.split('\t') for row in file]

#Sumar columna 2
suma = 0
for i in file:
    suma += int(i[1])
print(suma)