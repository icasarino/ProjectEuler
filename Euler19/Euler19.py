anios = list(range(1901,2001))
aniosBisiestos = list(filter(lambda x: x % 4 == 0,anios))

def esBisiesto(anio):
	return anio in aniosBisiestos

def cantDias(anio):
	return 366 if esBisiesto(anio) else 365
def primerDiaAnio(anio,diaInicialAnioAnterior):
	dias = cantDias(anio)
	return (diaInicialAnioAnterior + dias) % 7
def setDiaInicial(tlist):
	for i in range(len(tlist)):
		tupla = tlist[i]
		if tupla[0] == 1901:
			tlist[i] = (tupla[0],primerDiaAnio(tupla[0],1))
		else:
			if esBisiesto(tlist[i][0]):
				t = (tupla[0],(primerDiaAnio(tupla[0],tlist[i - 1][1]) - 1) % 7)
			elif esBisiesto(tlist[i - 1][0]):
				t = (tupla[0],(primerDiaAnio(tupla[0],tlist[i - 1][1]) + 1) % 7)
			else:
				t = (tupla[0],(primerDiaAnio(tupla[0],tlist[i - 1][1])) % 7)
			tlist[i] = t
def setDiaInicialMeses(tupla):

	anio = tupla[0]
	diaInicio = tupla[1]

	cantDiasBase = [31,29 if esBisiesto(anio) else 28,31,30,31,30,31,31,30,31,30,31]
	lista = []
	for i in range(len(cantDiasBase) - 1):
		lista.append((diaInicio + cantDiasBase[i]) % 7)
		diaInicio = (diaInicio + cantDiasBase[i]) % 7

	return lista




# aniosResult = [(anio,diaInicio,[diaInicioMes])...]
aniosResult = list(map(lambda anio: (anio,0),anios))

setDiaInicial(aniosResult)

for i in range(len(aniosResult)):
	tupla = aniosResult[i]
	aniosResult[i] = (tupla[0],tupla[1],len(list(filter(lambda num: num == 0,setDiaInicialMeses(tupla)))))

res = 0
for tupla in aniosResult:
	res += tupla[2]
	if tupla[1] == 0:
		res += 1
print("Resultado: ",res)
#for i in range(6):
#	print(aniosResult[i])

#print(aniosResult)


