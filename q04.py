## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3

#leer archivo
file = open('data.csv', 'r').readlines()

#Eliminar \n al final
file = [row[0:-1] for row in file]

#Separar por tab
file = [row.split('\t') for row in file]

result = {}

for element in file:
	result[element[2].split('-')[1]] = 0

for element in file:
	result[element[2].split('-')[1]] = result[element[2].split('-')[1]] + 1

for key in sorted(result.keys()):  
    print(key + ',' + str(result[key]))