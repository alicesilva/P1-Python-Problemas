#coding: utf-8

def busca_matriz(m,e):
	cont = 0
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				a = i
				b = j
				cont += 1
				break
		break
	
	if cont == 0:
		return None
	else:
		tupla = (a,b)
		return tupla
