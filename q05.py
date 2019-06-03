## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1

#leer archivo
file = open('data.csv', 'r').readlines()

#Eliminar \n al final
file = [row[0:-1] for row in file]

#Separar por tab
file = [row.split('\t') for row in file]

result = {}

for element in file:
	result[element[0]] = []

for element in file:
	result[element[0]].append(int(element[1]))

for key in sorted(result.keys()):  
    print(key + ',' + str(max(result[key])) + ',' + str(min(result[key])))