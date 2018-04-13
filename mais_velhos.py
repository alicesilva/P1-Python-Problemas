#coding: utf-8
def idosos_inicio(fila):
	cont = 0
	for i in range(len(fila)):
		if fila[i] >= 60:
			fila[i], fila[cont] = fila[cont], fila[i]
			cont += 1
	return
