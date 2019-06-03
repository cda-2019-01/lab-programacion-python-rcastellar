## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
#leer archivo
file = open('data.csv', 'r').readlines()

#Eliminar \n al final
file = [row[0:-1] for row in file]

#Separar por tab
file = [row.split('\t') for row in file]

data = []
i = 0
for element in file:
	data.append([])
	for e in element:
		a = e.split(',')
		if(len(a) == 1):
			data[i].append(a[0])
		else:
			data[i].append(a)
	i += 1

result = {}

for element in data:
	for el in element[4]:
		aux = el.split(':')
		result[aux[0]] = 0

for element in data:
	for i in element[4]:
		aux = i.split(':')
		result[aux[0]] += 1

for i in sorted(result):
    print(i + ',' + str(result[i]))

