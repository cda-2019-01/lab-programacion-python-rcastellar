
## Por cada clave de la columna 5 (cadena de tres letras), obtenga 
## el valor mas pequeno y el valor mas grande asociado a esa clave.
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5

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
		result[aux[0]] = []

for element in data:
	for el in element[4]:
		aux = el.split(':')
		result[aux[0]].append(int(aux[1]))

# print result

for key in sorted(result.keys()):  
    print(key + ',' + str(min(result[key])) + ',' + str(max(result[key])))