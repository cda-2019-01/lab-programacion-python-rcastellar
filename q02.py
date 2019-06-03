## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14

#leer archivo
file = open('data.csv', 'r').readlines()

#Eliminar \n al final
file = [row[0:-1] for row in file]

#Separar por tab
file = [row.split('\t') for row in file]

result = {}

for element in file:
	result[element[0]] = 0

for element in file:
	result[element[0]] = result[element[0]] + 1

for key in sorted(result.keys()):  
    print(key + ',' + str(result[key]))