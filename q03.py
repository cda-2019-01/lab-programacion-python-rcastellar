## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67

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
	result[element[0]] = result[element[0]] + int(element[1])

for key in sorted(result.keys()):  
    print(key + ',' + str(result[key]))